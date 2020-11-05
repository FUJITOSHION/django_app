from django.db.models.query import QuerySet
from django.http import request
from sns.models import Friend
from django.shortcuts import render
from django.http import HttpResponse#アクセスに送り返すもの
from .forms import SnsForm
from django.views.generic import TemplateView
from django.db.models import QuerySet

def __new_str__(self):
    result = ''
    for item in self:
        result += '<tr>'
        for k in item:
            result += '<td>' +str(k) + '=' + str(item[k]) + '</td>'
        result += '</tr>'
    return result

QuerySet.__str__ = __new_str__

def index(request):
    data = Friend.objects.all().values('id','name','age')
    params = {
        'title':'Hello',
        'data':data,
    }
    return render(request, 'sns/index.html', params)