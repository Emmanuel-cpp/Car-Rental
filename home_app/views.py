from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import logout

# Create your views here.
def index(request):
    return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname'].title()
        lastname = request.POST['lastname'].title()
        email = request.POST['email']
        password = request.POST['password1']
        password1 = request.POST['password2']
        
        if password==password1:
            if User.objects.filter(email=email).exists():
                messages.info(request,"The Email Address you entered is already in use")
                return redirect('signup')
            else: 
                user = User.objects.create_user(username=firstname,first_name=firstname,last_name=lastname,email=email,password=password1)
                user.save();
                return redirect('login')
        else: 
            messages.info(request,"The password you entered do not match")
            
    return render(request, 'registration.html')

#LOGIN FUNCTION/VIEW
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"Logged in successfully")
            return redirect('index')
        else: 
            messages.info(request,"Invalid Login Credentials")
            return redirect('login')
    else: 
        return render(request,'login.html')    

def home_2(request):
    return render(request,'home-two.html')    

def about(request):
    return render(request, 'about.html')

def carList1(request):
    return render(request, 'car-list-one.html')
def carList2(request):
    return render(request, 'car-list-two.html')

def reservation(request):
    return render(request, 'reservation.html')

def error404(request):
    return render(request, 'error-404.html')

def blog(request):
    return render(request, 'blog.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def contact(request):
    return render(request, 'contact.html')