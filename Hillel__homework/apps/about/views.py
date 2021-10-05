from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Привет мир')


def source_code(request):
    import inspect
    source_code = inspect.getsource(inspect.getmodule(inspect.currentframe()))
    data = {"source_code":source_code}
    return render(request, 'source_code.html', context=data)


def whoami(request):
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
    data = {"browser": browser, 'ip': ip, 'now_time': now_time}
    return render(request, 'index.html', context=data)
