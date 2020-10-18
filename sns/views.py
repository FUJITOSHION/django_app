from django.shortcuts import render
from django.http import HttpResponse#アクセスに送り返すもの


def index(request):
    params = {
        'title':'sns/index',
        'msg':'お名前は？',
        # 'goto':'next',
    }
    return render(request, 'sns/index.html', params)


# def next(request):
    # params = {
    #     'title':'sns/next',
    #     'msg':'next page',
    #     'goto':'index',
    # }
    # return render(request, 'sns/index.html', params)


def form(request):
    msg = request.POST['msg']
    params = {
        'title':'sns/form',
        'msg':'こんにちは、'+msg+'さん',
    }
    return render(request, 'sns/index.html', params)


