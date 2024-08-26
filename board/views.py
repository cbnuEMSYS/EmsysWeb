from django.shortcuts import render, redirect

def test(request):
    return redirect('main:mainpage')

#def board_list(request):
#    return render(request, 'board/board_list.html')

def board_list(request):
    context = {
        'title': 'Board list',
        'board_list': [
            {'no':1, 'title': '목록1' },
            {'no':2, 'title': '목록2' },
            {'no':3, 'title': '목록3' },
            {'no':4, 'title': '목록4' },
            {'no':5, 'title': '목록5' }
        ]
    }
    return render(request, 'board/board_list.html', context)