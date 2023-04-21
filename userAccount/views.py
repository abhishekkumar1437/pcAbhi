from django.contrib.auth import authenticate
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import login
from products.models import Category
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request,'home.html')

def index(request):
    category=Category.objects.all().values()
    category={
        'category':category,
    }
    return render(request,'index.html',category)

def signin(request):
    #name=username
    #password=password
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=authenticate(request,username=username,password=password)
        
        
       
        if user is not None:
            login(request,user)
            #messages.info(request,"Login successful")
            
            return redirect('home')
        else:
            messages.error(request,'invalid username or password')
            return redirect('signin')
    else:
        return render(request,'login.html')






def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password2']
        if password==cpassword:
            if User.objects.filter(email=email).exists():
                messages.error(request,'Email already registered !')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                messages.info(request,'User created go to signin page ')
                return redirect('signin')
        else:
            messages.error(request,'Password did not match ')
            return redirect('signup')
    else:
        return render(request,'signup.html')



def logout(request):
    auth.logout(request)
    return redirect('home')


def forget_password(request):
    return render(request,'forget_password.html')