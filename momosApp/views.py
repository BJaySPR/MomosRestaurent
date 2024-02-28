from django.shortcuts import render
from .models import Get_in_touch
from datetime import datetime

# Create your views here.
def index(request):
    if request.method=='POST':
        name =request.POST['name']
        email =request.POST['email']
        phone_no = request.POST['phone']
        message = request.POST['message']
        regi = Get_in_touch(name=name,email=email,phone_no=phone_no,message=message)
        regi.save()
    current_date = datetime.now() 
    return render(request, 'index.html',{'date':current_date})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method=='POST':
        name =request.POST['name']
        email =request.POST['email']
        phone_no = request.POST['phone']
        message = request.POST['message']
        regi = Get_in_touch(name=name,email=email,phone_no=phone_no,message=message)
        regi.save()

    return render(request, 'contact.html')
def menu(request):
    return render(request,'menu.html')
def service(request):
    return render(request, 'services.html')
               