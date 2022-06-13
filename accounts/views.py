from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from django.contrib.auth import authenticate, login, logout
import face_recognition
from PIL import Image, ImageDraw
from .forms import CreateUserForm,BlogCreate
from .models import *
import os

@unauthenticated_user
def Login(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)
    

def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def freelance(request):
    upload = BlogCreate()
    if request.method == 'POST':
        upload = BlogCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('home')
    else:
        return render(request, 'accounts/freelance.html', {'freelance':upload})



@login_required(login_url='login')
def home(request):
    profile = Add.objects.all()
    context = {'profile':profile}
    return render(request, 'accounts/home.html', context)


@unauthenticated_user
def Register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            #messages.success(request, 'Account was created for ' + username)
            return redirect('home')

            

    context = {'form':form}
    return render(request, 'accounts/register.html', context)

@login_required(login_url='login')
def delete(request, pk):
    prod = Add.objects.get(id=pk)
    if len(prod.image) > 0:
        os.remove(prod.image.path)
    prod.delete()
    #messages.success(request,"Product Deleted Successfuly")
    return redirect('home')

@login_required(login_url='login')     
def update(request, blog_id):
    blog_id = int(blog_id)
    try:
        blog_sel = Add.objects.get(id = blog_id)
    except Add.DoesNotExist:
        return redirect('home')
    blog_form = BlogCreate(request.POST or None, instance = blog_sel)
    if blog_form.is_valid():
       blog_form.save()
       return redirect('home')
    return render(request, 'accounts/update.html', {'freelance':blog_form})
         




   