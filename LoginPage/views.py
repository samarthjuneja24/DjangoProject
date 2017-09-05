import os
from django.dispatch import receiver
from django.db import models
from django.shortcuts import render,redirect
from .forms import UserForm
from .models import User,Video,UserProfile
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
def loginform(request):
    return render(request,'LoginPage/forma/index.html')

def signup(request):
    return render(request,'LoginPage/forma/index.html')

def choice(request):
    return render(request,'LoginPage/forma/index.html')
def _delete_file(path):
    if os.path.isfile(path):
        os.remove(path)

@receiver(models.signals.post_delete,sender=Video)
def delete_file(sender,instance,*args,**kwargs):
    if instance.video:
        _delete_file(instance.video.path)

@login_required(login_url='login/')
def add_model(request):
    error=False
    context=RequestContext(request)
    registered=False
    form=UserForm(request.POST)
    username=form.data['username']
    if User.objects.filter(username=username).exists():
        messages.add_message(request,messages.ERROR,'Username already exists')
        return render(request,'LoginPage/forma/index.html',{'error':error},context)
    else:
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            registered=True
            error=False
        else:
            print (form.errors)
        return render (request,'LoginPage/forma/index.html',{'user_form':form, 'registered':registered, 'error':error},context)

def find_model(request):
    if request.method=='POST':
        context={
        }
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                request.session['username']=username
                request.session['password']=password
                login(request, user)
                tempuser=User.objects.get(pk=user.pk)
                tempuserp=UserProfile.objects.get(user=tempuser)
                context={
                    'username':user.username,
                    'name':user.first_name+" "+user.last_name,
                    'profile_pic':tempuserp.profile_pic,
                    'password':password,
                }
                #request.sessions['username']=username
                #request.sessions['password']=password
                populateContext(request, context)
                return render(request,'AfterLogin/profile.html',context)
            else:
                populateContext(request, context)
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details: {0}, {1}".format(username, password))
            messages.add_message(request,messages.ERROR,'Please Login first')
            return render(request,'LoginPage/forma/index.html',context)
    elif request.method=='GET':
        return render(request,'LoginPage/forma/index.html')

def upload(request):
    if request.method == 'POST':
        username=request.POST['username']
        auser=User.objects.get(username=username)
        tempuser=UserProfile.objects.get(user=auser)
        tempuser.profile_pic=request.FILES['profile_pic']
        tempuser.save()
        context={
                    'name':auser.first_name + " " + auser.last_name,
                    'username':auser.username,
                    'profile_pic':tempuser.profile_pic
                }
        if auser:
            return render(request,'AfterLogin/profile.html',context)
        else:
            return HttpResponse('Invalid username or password')
    else:
        return HttpResponse('Please login first')

def uploadvideo(request):
    if request.method == 'POST':
        username=request.POST['username']
        owner=User.objects.get(username=username)
        tempuser=UserProfile.objects.get(user=owner)
        if tempuser:
            tempvideo=Video(video=request.FILES['video'], username=tempuser)
            tempvideo.save()
            context={
                'username':username,
                'link':tempvideo.video,
            }
            return render(request,'AfterLogin/uploads.html',context)
        else:
            return HttpResponse('Please login to view this page')
    else:
        return HttpResponse('Please Login to view this page')

"""def login(request):
    context = {}
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
            else:
                context['error']='Non active user'
        else:
            context['error'] = 'Wrong username or password'
    except:
        context['error'] = ''

    populateContext(request, context)
    return render(request, 'index.html', context)
"""
def logout1(request):
    context = {}
    try:
        del request.session['username']
        logout(request)
    except:
        context['error'] = 'Some error occured.'

    populateContext(request, context)
    return render(request, 'LoginPage/forma/index.html', context)

def populateContext(request, context):
    context['authenticated'] = request.user.is_authenticated()
    if context['authenticated'] == True:
        context['username'] = request.user.username

def usermainview(request):
    username=request.POST['username']
    videolist=Video.objects.select_related('username').filter(username__user__username=username)
    print(videolist)
    print('hi')
    return render(request,'AfterLogin/main.html',{'videolist':videolist})