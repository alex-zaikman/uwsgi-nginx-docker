import json

import pandas as pd
from flask import Flask, request, make_response

application = Flask(__name__)


@application.route("/ping", methods=['GET'])
def ping():
    return ''


@application.route("/invocations", methods=['POST'])
def invocations():
    req_data = request.get_data()
     # TODO
    resp = make_response(json.dumps({'echo': req_data}))
    resp.headers['Content-Type'] ='application/json'
    return resp
