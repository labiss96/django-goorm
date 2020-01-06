from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:   
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)   #로그인 상태를 유지시켜주는 함수임
               

                return redirect('accounts:login')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'accounts/signup.html')
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:   #유저가 none 이 아니면은 로그인 조져라  그다음에 홈창으로 가주는거임
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')          #그냥 단순하게 로그아웃 상태가 해체된다