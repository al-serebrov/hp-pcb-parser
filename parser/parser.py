import json

import requests


def get_images_info(part_number):
    resp = requests.get(
        'https://pcb.itcs.hp.com/api/catalogs/us-en/\
    nodes/search/autocomplete?query={}&status[]=O&status[]=L'
        .format(part_number)
    )

    results = resp.json().get('results')

    oids = [res.get('oid') for res in results]
    print(oids)

    for oid in oids:
        resp = requests.get(
            'https://pcb.itcs.hp.com/api/catalogs/\
    us-en/nodes/{}/contents/I?status[]=O&status[]=L&hierParadigm=F'.format(oid)
        )
        print(json.dumps(resp.json(), indent=2))
