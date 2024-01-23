from django.shortcuts import render
from django.http import HttpResponse
from app.form import *
from app.models import *
# Create your views here.

def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
        return HttpResponse('Topic are inserted successfuly')
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
        return HttpResponse('Webpage are inserted successfuly')
    return render(request,'insert_webpage.html',d)


def insert_acces(request):
    EAFO=AccessRecordForm()
    d={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=AccessRecordForm(request.POST)
        if AFDO.is_valid():
            AFDO.save()
        return HttpResponse('Acceessrecord  are inserted successfuly')
    return render(request,'insert_acces.html',d)
