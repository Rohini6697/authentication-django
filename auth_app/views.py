from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        confirm = request.POST.get('conf_password')

        if password == confirm:
            if User.objects.filter(username = user_name).exists():
                return render(request,'sign_up.html',{'error': 'Person Already Exists' })
            user = User.objects.create_user(username = user_name,password=password)
            user.save()
            return render(request,'login.html') 
        else:
            return render(request,'sign_up.html') 
    else:
        return render(request,'sign_up.html') 
@login_required
def dashboard(request):
    return render(request,'Dashboard.html')


def user_login(request):
    if request.method == 'POST':
        login_name = request.POST.get('login_name')
        login_pass = request.POST.get('login_pass')

        user = authenticate(username=login_name,password=login_pass)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return render(request,'login.html',{'error':'no account found'})
    else:
        return render(request,'login.html')
def  user_logout(request):
    logout(request)
    return redirect('login')