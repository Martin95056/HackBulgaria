from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import User


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', locals())

    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.all().filter(email=email)
        if len(user) == 0:
            user1 = User(email=email, password=password)
            user1.save()
            return render(request, 'user_registered.html', locals())
        else:
            return render(request, 'user_exists.html', locals())


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', locals())

    session_email = request.session.get('email', False)
    if session_email:
        return HttpResponseRedirect('/profile/')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User.objects.all().filter(email=email)
            if len(user) == 1:
                request.session['email'] = email
                request.session.flush()
                return HttpResponseRedirect('/profile/')
            else:
                return HttpResponseRedirect('/register')


def profile(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    return render(request, 'profile.html', locals())
