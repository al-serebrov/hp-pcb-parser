import json

from parser import parser

from flask import Flask, abort, render_template, request


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
    images_info = parser.get_images_info(part_number)
    return render_template('images.html', images_info=images_info)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
