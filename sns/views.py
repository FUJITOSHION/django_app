from sns.models import Friend
from django.shortcuts import render
from django.http import HttpResponse#アクセスに送り返すもの
from .forms import SnsForm
from django.views.generic import TemplateView

def index(request):
    data = Friend.objects.all()
    params ={
        'title':'Hello',
        'message':'all freineds',
        'data':data,
    }
    return render(request, 'sns/index.html', params)