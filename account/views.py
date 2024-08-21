from django.shortcuts import render, redirect

def test(request):
    return redirect('main:mainpage')

def board_list(request):
    return render(request, 'board/board_list.html', {})