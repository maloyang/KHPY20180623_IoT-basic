# coding=UTF-8
from __future__ import unicode_literals

from flask import Flask, request

import pprint

import json
import requests

#------
#   line nofity功能 web-api
#------

app = Flask(__name__)

@app.route('/')
def homepage():
    return "OK"


###############
# Line API
###############
# group notify token 'lEwq4fFJtphsPwkvqHwdb92g6nrqXS6bYn56kL068sP'
@app.route('/line', methods=['GET', 'POST'])
def line():
    url = "https://notify-api.line.me/api/notify"

    token = request.args.get('token')
    message = request.args.get('message')

    headers = {"Authorization" : "Bearer "+ token}

    payload = {"message" :  message}

    try:
        r = requests.post(url ,headers = headers ,params=payload)
    except Exception as ex:
        print('line_notify() error: ', str(ex))
        return 'ERROR'
    
    return 'OK'

@app.route('/line2', methods=['GET', 'POST'])
def line2():
    url = "https://notify-api.line.me/api/notify"

    print('--.__dict__--')
    pprint.pprint(request.__dict__)
    print('--.data--')
    pprint.pprint(request.data)
    print('--.form--')
    pprint.pprint(request.form)
    print('--.args--')
    pprint.pprint(request.args)
    print('----')

    '''
    token = request.form['token']
    message = request.form['message']
    print(token, message)
    '''
    data = json.loads(request.data)
    token = data['token']
    message = data['message']

    headers = {"Authorization" : "Bearer "+ token}

    payload = {"message" :  message}

    try:
        r = requests.post(url ,headers = headers ,params=payload)
    except Exception as ex:
        print('line_notify() error: ', str(ex))
        return 'ERROR: '+str(ex)
    
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
