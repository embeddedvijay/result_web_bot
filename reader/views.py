from django.shortcuts import render,HttpResponse,redirect
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def group_automatic_bot(request):
    template = loader.get_template('pricing.html')
    return HttpResponse(template.render())