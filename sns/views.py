from django.shortcuts import render
from django.http import HttpResponse#アクセスに送り返すもの


def index(request):
    if 'msg' in request.GET:
        msg = request.GET['msg']
        result = 'you typed:' + msg
    else:
        result = 'please send msg'
    return HttpResponse(result)

