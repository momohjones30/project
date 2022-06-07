from django.shortcuts import render

# Create your views here.


def mainpage(request):
    return render (request, 'Indexpage.html')


# def stafflogin(request):
#     return render(request, 'stafflogin.html')

# def studentlogin(request):
#     return render(request, 'studentlogin.html')