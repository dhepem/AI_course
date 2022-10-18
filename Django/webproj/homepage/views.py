from http.client import HTTPResponse
from django.shortcuts import HttpResponse, render

# Create your views here.


def index(request):
    # return HttpResponse("<h1>Hello World!</h1>")
    nums = [1, 2, 3, 4, 5]

    return render(request, 'index.html', {"my_list": nums})
