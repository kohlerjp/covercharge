from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from posts import urls
import sys

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def new(request):
	
	return render(request,'users/new.html',{})
def create(request):
	user = User.objects.create_user(request.POST['email'],request.POST['email'],request.POST['password'])
	user.save()
	user = authenticate(username=request.POST['email'],password=request.POST['password'])
	login(request,user)
	return redirect('posts:index')
def logout_view(request):
	logout(request)
	return redirect('posts:index')
def login_view(request):
	return render(request,'users/login.html',{})
def login_action(request):
	user = authenticate(username=request.POST['email'],password=request.POST['password'])
	login(request,user)
	return redirect('posts:index')