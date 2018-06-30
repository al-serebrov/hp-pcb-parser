"""
Retrieve images information from HP Product Content Browser.
"""

import requests


def get_images_info(part_number):
    """
    Get images infromation from HP PCB.

    Arguments:
        part_number - string with part number, e.g. XZ812UT

    Returns:
        images_info - JSON (list of dictionaries) with images info
            for example:
            [
                "path": [
                {
                  "baseProdname": "Desktops & Workstations",
                  "oid": 12454,
                  "level": 1
                },
                ...
                ],
                "baseProdname": "HP 100B All-in-One PC (ENERGY STAR)",
                "prodname": "HP 100B All-in-One PC (ENERGY STAR)",
                "contents": [
                {
                  "imageUrlHttp": "http://product-images.www8-hp.com/...",
                  "dpiResolution": "72",
                  "pixelWidth": "64",
                  "imageUrlHttps": "https://ssl-product-images.www8-hp.com/..",
                  "tag": "c02292560.jpg",
                  "background": "White",
                  "name": "c02292560.jpg",
                  "lbl": "Right profile closed | White | 72 | 64 | 64 | jpg",
                  "languageCode": null,
                  "fullTitle": "HP Omni 100-5000 Desktop PC series",
                  "orientation": "Right profile closed",
                  "fileSize": 1126,
                  "contentType": "jpg",
                  "disclosureLevel": "Public",
                  "pixelHeight": "64",
                  "val": "http://product-images.www8-hp.com/..."
                },
                ...
            ]
            """
    resp = requests.get(
        'https://pcb.itcs.hp.com/api/catalogs/us-en/\
    nodes/search/autocomplete?query={}&status[]=O&status[]=L'
        .format(part_number)
    )

    results = resp.json().get('results')

    oids = [res.get('oid') for res in results]

    images_info = []
    for oid in oids:
        resp = requests.get(
            'https://pcb.itcs.hp.com/api/catalogs/\
    us-en/nodes/{}/contents/I?status[]=O&status[]=L&hierParadigm=F'.format(oid)
        )
        images_info.append(resp.json())
    return images_info


def get_catalogs():
    """Get available HP catalogs.

    Returns:
        catalogs - dictionary with catalogs information, for example:
        {
            "ww-en":{"code":"ww-en","id":5,"name":"WW EN"},
            "na-en":{"code":"na-en","id":3,"name":"North America Region"},
            "us-en":{"code":"us-en","id":4,"name":"United States"},
            ...
        }
    """
    catalogs = requests.get('https://pcb.itcs.hp.com/api/catalogs').json()
    return catalogs