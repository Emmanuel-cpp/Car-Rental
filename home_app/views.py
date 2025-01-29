from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
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

