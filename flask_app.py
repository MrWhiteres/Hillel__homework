#!/usr/bin/python3
import random
import string
from flask import Flask, request, render_template, url_for

app = Flask('My first app')
app.config["APPLICATION_ROOT"] = "/app"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/whoami')
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
    return render_template('whoami.html', browser=browser, ip=ip, now_time=now_time)


@app.route('/source_code')
def Source_code():
    import inspect
    source_code = inspect.getsource(inspect.getmodule(inspect.currentframe()))
    return render_template('source_code.html', source_code=source_code)


def get_random_str(length, specials, digits):
    error = None
    try:
        length = int(length)
    except ValueError:
        return None, 'Length should be int'
    if 1 > length or length > 100:
        return None, 'Length should be 1~100'
    if digits not in (None, '1'):
        return None, 'Digits Should be 0 or 1'
    if specials not in (None, '1'):
        return None, 'Specials Should be 0 or 1'

    ran_choi = string.ascii_letters
    if specials:
        ran_choi += string.punctuation
    if digits:
        ran_choi += string.digits

    result = ''
    if length and not error:
        result = ''.join(random.choices(ran_choi, k=length))

    return result, None


@app.route(f'/random', methods=['GET', 'POST'])
def string_element():
    length = request.args.get('length', -1)
    specials = request.args.get('specials')
    digits = request.args.get('digits')

    result, error = get_random_str(length, specials, digits)

    return render_template('random.html', result=result, error=error)


if __name__ == '__main__':
    app.run(debug=True)
