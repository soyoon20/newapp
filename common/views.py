from django.shortcuts import render, redirect

from django.contrib import auth
from django.contrib.auth import authenticate, login
from common.forms import UserForm

def logout(request):
    auth.logout(request)
    return redirect('index')
# 0419 회원가입 함수 생성
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

# Create your views here.
