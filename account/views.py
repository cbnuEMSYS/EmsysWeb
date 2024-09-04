from django.shortcuts import render, redirect

def test(request):
    return redirect('main:mainpage')

def logout(request):
    return render(request, 'account/login.html')

def login(request):
    return render(request, 'account/login.html')

def register(request):
    return render(request, 'account/register.html')