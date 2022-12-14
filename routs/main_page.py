import flask, time
from flask import request, jsonify
from __main__ import application

from flask import make_response


@application.route('/', methods=['GET'])
def main():
    return jsonify({'kek': 'kek'})
