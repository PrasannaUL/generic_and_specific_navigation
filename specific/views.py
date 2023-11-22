from django.shortcuts import render

# Create your views here.


def sahana(request):
    return render(request,'sahana.html')


def sruthi(request):
    return render(request,'sruthi.html')
