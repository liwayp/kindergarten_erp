from django.shortcuts import render, redirect
from django.contrib.auth import login,  logout
# from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')  
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

