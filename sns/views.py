from django.db.models.query import QuerySet
from django.http import request
from sns.models import Friend
from django.shortcuts import redirect, render
from django.http import HttpResponse#アクセスに送り返すもの
from .forms import FriendForm
from django.views.generic import ListView, DetailView
from django.db.models import QuerySet
from .forms import FindForm

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

def create(request):
    if (request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title':'Hello',
        'form':FriendForm(),
    }
    return render(request, 'sns/create.html', params)


def edit(request, num):
    obj = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'titile':'Hello',
        'id':num,
        'form':FriendForm(instance=obj)
    }
    return render(request, 'sns/edit.html', params)

def delete(request, num):
    friend = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend.delete()
        return redirect(to='/hello')
    params = {
        'title':'hello',
        'id':num,
        'obj':friend,
    }
    return render(request, 'sns/delete.html', params)

class FriendList(ListView):
    model = Friend

class FriendDetail(DetailView):
    model = Friend

def find(request):
    if (request.method == 'POST'):
        form = FindForm(request.POST)
        find = request.POST['find']
        data = Friend.objects.filter(name__contains=find)
        msg = 'Result:' + str(data.count())

    else:
        msg = 'search words ...'
        form = FindForm()
        data = Friend.objects.all()

    params = {
        'title':'Hello',
        'message':msg,
        'form':form,
        'data':data
    }
    return render(request, 'sns/find.html', params)