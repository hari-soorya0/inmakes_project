from django.shortcuts import render
from django.http import HttpResponse
from .models import place


# Create your views here.
def demo(request):
    # return HttpResponse('Hello world')
    # return render(request, 'index2.html')         ## to run the addition program
    return render(request, 'index.html')        ## to run the static template page


# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     add = x + y
#     return render(request, 'results.html', {'addition': add})

