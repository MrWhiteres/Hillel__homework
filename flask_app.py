#!/usr/bin/python3
import random
import string
from flask import Flask, request

app = Flask('My first app')


@app.route('/')
def index():
    return f"""
        <html>
         <head>
            <title>Tutorial page</title>
         </head>
         <body>
         <h1>General list</h1>
         <a href='http://127.0.0.1:5000/random'>If you need random string, click here</a><br/>
         <a href='http://127.0.0.1:5000/whoami'>If you need 
         information of your browser, ip and server time, click here</a><br/>
         <a href='http://127.0.0.1:5000/source_code'>if you need source code, click here</a>
         </body> 
        </html>
          """


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
    return f"""
        <html>
         <head>
            <title>User info</title>
         </head>
         <body>
          <p>Your browser - {browser}</p>
          <p>ip - {ip}</p>
          <p>Server data and time - {now_time}</p>
         </body> 
        </html>
          """


@app.route('/source_code')
def source_code():
    import inspect
    return inspect.getsource(inspect.getmodule(inspect.currentframe()))


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

    return f"""
    <html>
     <head>
        <title></title>
     </head>
     <body>
        <h1>Random generator</h1> 
     <form method='GET'>
        length: <input type='number' name='length' value={length}/><br/>
        specials: <input type='checkbox' name='specials' value='1'/><br/>
        digits: <input type='checkbox' name='digits' value='1'/><br/>
        <input type = 'submit'/>
        <h2>Result = {result}</h2>
        <font text='red'>{error if error else ''}</font>
     </form>
     </body> 
    </html>
      """


if __name__ == '__main__':
    app.run(debug=True)
