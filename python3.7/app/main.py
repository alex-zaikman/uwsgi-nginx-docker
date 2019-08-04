import json

import pandas as pd
from flask import Flask, request, make_response

app = Flask(__name__)


@app.route("/ping", methods=['GET'])
def ping():
    return ''


@app.route("/invocations", methods=['POST'])
def invocations():
    req_data = request.get_data()
     # TODO
    resp = make_response(json.dumps({'echo': req_data}))
    resp.headers['Content-Type'] ='application/json'
    return resp
