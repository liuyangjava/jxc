from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from django.core.context_processors import request
from django.http.response import HttpResponseRedirect
# Create your views here.

def index(request):
    return render_to_response('order/index.html')

@csrf_exempt
def order_login(request):
    userName=request.POST['userName']
    passWord=request.POST['passWord']
    print("userName:"+userName)
    print("passWord:"+passWord)
    #print(username=userName,password=passWord)
    user=authenticate(username=userName,password=passWord)
    
    if user is  None:
         
        return render_to_response('order/error.html')
    else:
        login(request, user)    
        print(request.user)   
    
    return HttpResponseRedirect('/order/main.php')

@csrf_exempt
def order_main(request):
    main_params={'user':request.user}
    return render_to_response('order/main.html',main_params)
    