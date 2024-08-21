from django.shortcuts import render, redirect

def test(request):
    return redirect('main:mainpage')