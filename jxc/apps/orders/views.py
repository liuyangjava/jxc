from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render_to_response('order/index.html')

@csrf_exempt
def order_login(request):
    userName=request.POST['userName']
    passWord=request.POST['passWord']
    print("userName:"+userName)
    print("passWord:"+passWord)
    return render_to_response('order/main.html')
