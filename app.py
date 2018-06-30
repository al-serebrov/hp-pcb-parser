import json

from flask import Flask, abort, render_template, request

from .parser import parser


app = Flask(__name__)


with open('queries.json', 'r') as filename:
    queries_list = json.load(filename)


@app.route('/', methods=['GET'])
def get_index():
    catalogs = parser.get_catalogs()
    return render_template('index.html', catalogs=catalogs)


@app.route('/<part_number>', methods=['GET'])
def get_images(part_number):
    images_info = parser.get_images_info(part_number)
    return render_template('queries.html', images_info=images_info)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
