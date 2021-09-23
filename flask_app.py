#!/usr/bin/python3
import random
from flask import *

app = Flask('My first app')


@app.route('/')
def home():
    return 'hello world!'


@app.route('/whoami/')
def who_am_i():
    import httpagentparser
    import socket
    import datetime
    agent = request.environ.get('HTTP_USER_AGENT')
    browser = httpagentparser.detect(agent)
    if not browser:
        browser = agent.split('/')[0]
    else:
        browser = browser['browser']['name']
    ip = socket.gethostbyname(socket.getfqdn())
    now = datetime.datetime.now()
    now_time = now.strftime("%d-%m-%Y %H:%M")
    return f'{browser}, {ip}, {now_time}'


@app.route('/source_code/')
def source_code():
    import inspect
    return inspect.getsource(inspect.getmodule(inspect.currentframe()))


@app.route(f'/random')
def string_element():
    length = request.args.get('length')
    specials = request.args.get('specials')
    digits = request.args.get('digits')
    str_print = ''
    eng_alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    spec_sim = '!"№;%:?*()_+.'
    dig_sim = '0123456789'
    if (int(length) < 0 or int(length) > 100) and (int(specials) != 0 or int(specials) != 1) and (
            int(digits) != 0 or int(digits) != 1):
        return 'Параметр Length (должен быть в диапазоне 0 до 100 , Параметр Specials и Digits должны быть равны 0 или 1'
    else:
        if int(specials) == int(digits) == 0:
            for i in range(int(length)):
                str_print += random.choice(eng_alphabet)
        if int(specials) == 1 and int(digits) == 0:
            for i in range(int(length)):
                str_print += random.choice(eng_alphabet + spec_sim)
        if int(specials) == 0 and int(digits) == 1:
            for i in range(int(length)):
                str_print += random.choice(eng_alphabet + dig_sim)
        if int(specials) == 1 and int(digits) == 1:
            for i in range(int(length)):
                str_print += random.choice(eng_alphabet + spec_sim + dig_sim)
    return str_print


if __name__ == '__main__':
    app.run(debug=True)
