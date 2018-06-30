import json

from parser import parser

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_index():
    catalogs_raw = parser.get_catalogs()
    catalogs = []
    for key, value in catalogs_raw.items():
        catalogs.append(value)
    sorted_catalogs = sorted(catalogs, key=lambda k: k['name'])
    return render_template('index.html', catalogs=sorted_catalogs)


@app.route('/<part_number>', methods=['GET'])
def get_images(part_number):
    market = request.args.get("market", "us-en")
    images_info = parser.get_images_info(part_number, market)
    parsed_contents = []
    for image_info in images_info:
        contents = image_info.get('contents')
        for content in contents:
            parsed_contents.append(content)
    sorted_contents = sorted(parsed_contents, key=lambda k: k['fileSize'])
    return render_template('images.html', contents=reversed(sorted_contents))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
