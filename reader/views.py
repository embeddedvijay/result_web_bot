from django.shortcuts import render,HttpResponse,redirect
from django.template import loader
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

from reader.common import *
from reader.save_model import *

login_cnt = 0

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def group_automatic_bot(request):
    template = loader.get_template('pricing.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def admin_loging(request):
    global login_cnt
    if request.method =='POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user:
            login_cnt = 0
            print(request, f'Login Successful.')
            template = loader.get_template('feature_select.html')
            return HttpResponse(template.render())
        else:
            if(login_cnt < 3):
                login_cnt += 1
                print(request, f'Password Incorrect !')
                template = loader.get_template('login_again.html')
                return HttpResponse(template.render())
            else:
                return HttpResponse("<h3>you have exit the limit ...</h3>")

    #template = loader.get_template('login.html')
    return HttpResponse("<h3>Hello ADMIN</h3>")

def add_group_result(request):
    
    return HttpResponse("<h3>welcome to add group result</h3>")

def add_personal_result(request):
    
    return HttpResponse("<h3>welcome to add personal result</h3>")


def configure_market_time(request):
    template = loader.get_template('update_market_time.html')
    return HttpResponse(template.render())

@csrf_exempt
def update_market_time(request):
    sridevi_day_op_time=request.POST.get('srdop')
    sridevi_day_cl_time=request.POST.get('srdcl')
    time_bazar_op_time=request.POST.get('tbop')
    time_bazar_cl_time=request.POST.get('tbcl')
    madhur_day_op_time=request.POST.get('madop')
    madhur_day_cl_time=request.POST.get('madcl')
    milan_day_op_time=request.POST.get('mldop')
    milan_day_cl_time=request.POST.get('mldcl')
    rajdhani_day_op_time=request.POST.get('rjdop')
    rajdhani_day_cl_time=request.POST.get('rjdcl')
    supreme_day_op_time=request.POST.get('spdop')
    supreme_day_cl_time=request.POST.get('spdcl')
    kalyan_day_op_time=request.POST.get('kldop')
    kalyan_day_cl_time=request.POST.get('kldcl')
    
    sridevi_nigh_op_time=request.POST.get('srnop')
    sridevi_nigh_cl_time=request.POST.get('srncl')
    main_bazar_op_time=request.POST.get('mainop')
    main_bazar_cl_time=request.POST.get('maincl')
    madhur_nigh_op_time=request.POST.get('manop')
    madhur_nigh_cl_time=request.POST.get('mancl')
    milan_nigh_op_time=request.POST.get('mlnop')
    milan_nigh_cl_time=request.POST.get('mlncl')
    rajdhani_nigh_op_time=request.POST.get('rjnop')
    rajdhani_nigh_cl_time=request.POST.get('rjncl')
    supreme_nigh_op_time=request.POST.get('supnop')
    supreme_nigh_cl_time=request.POST.get('supncl')
    kalyan_nigh_op_time=request.POST.get('klnop')
    kalyan_nigh_cl_time=request.POST.get('klncl')
    #data = update_data()
    
    save_market_time(sridevi_day_op_time,sridevi_day_cl_time,
                     time_bazar_op_time,time_bazar_cl_time,
                     madhur_day_op_time,madhur_day_cl_time,
                     milan_day_op_time,milan_day_cl_time,
                     rajdhani_day_op_time,rajdhani_day_cl_time,
                     supreme_day_op_time,supreme_day_cl_time,
                     kalyan_day_op_time,kalyan_day_cl_time,
                     sridevi_nigh_op_time,sridevi_nigh_cl_time,
                     main_bazar_op_time,main_bazar_cl_time,
                     madhur_nigh_op_time,madhur_nigh_cl_time,
                     milan_nigh_op_time,milan_nigh_cl_time,
                     rajdhani_nigh_op_time,rajdhani_nigh_cl_time,
                     supreme_nigh_op_time,supreme_nigh_cl_time,
                     kalyan_nigh_op_time,kalyan_nigh_cl_time)

    return HttpResponse("<h3>data has saved</h3>")
