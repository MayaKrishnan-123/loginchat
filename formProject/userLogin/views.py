from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse

from .form import registrationform
from .form import loginform
from .models import userlogin
from .form import Editform
from django.utils.safestring import mark_safe
import json


def room(request):
    user = request.user
    print(user)
    return render(request, 'registration/chat.html', {
        'room_name_json': mark_safe(json.dumps('lobby')), 'user': user})



def login(request):
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = loginform(request.POST)
        if request.method == 'POST':
            username = request.POST.get('username')
            password1 = request.POST.get("password1")
            if userlogin.objects.filter(username=username,password1=password1):
                response=redirect('../lobby/')
                return response
            else:
                return render(request,'registration/login.html')
        else:
            return render(request,'registration/login.html')
    else:
        # GET, generate blank form
        form = loginform()
    return render(request, 'registration/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = registrationform(request.POST)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 == password2:
            if userlogin.objects.filter(username=username).exists():
                print("username taken")
                return HttpResponse('username already exists')
            else:
                q = userlogin(first_name=first_name, last_name=last_name, username=username,
                              password1=password1)
                q.save()
                response = redirect('../login/')
                return response
    else:
        form = registrationform()
    return render(request,'registration/registrationform.html',{'form': form})



def home(request):
    return render(request,'registration/base.html')



def loginview(request):
    data=userlogin.objects.all()
    stu={"userlogin":data}
    return render_to_response("registration/data.html",stu)

def editprofile(request):
    if request.method == 'POST':
        form = Editform(request.POST)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')

        if form.is_valid():
            form.save()
            return redirect('../datashow')
    else:
        form = Editform()
        return render(request, 'registration/editprofile.html', {'form': form})



