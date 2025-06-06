from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddEmployeeForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Users


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('main') 
        else:
            return render(request, 'login.html', {'form': {'errors': True}})
    
    return render(request, 'login.html', {'form': {}})

def is_admin(user):
    return user.is_authenticated and user.role == 'admin'


@user_passes_test(is_admin)
def add_employee(request):
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main') 
    else:
        form = AddEmployeeForm()
    
    return render(request, 'add_employee.html', {'form': form})


@login_required
def employee_list(request):
    employees = Users.objects.exclude(role__in=['parents', 'admin'])
    return render(request, 'employee_list.html', {'employees': employees})


@login_required
def edit_employee(request, pk):
    user = get_object_or_404(Users, id=pk)
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            if form.cleaned_data['password']:
                user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('employee-list')
    else:
        form = AddEmployeeForm(instance=user)
    return render(request, 'add_employee.html', {'form': form})


@login_required
def delete_employee(request, pk):
    user = get_object_or_404(Users, id=pk)
    user.delete()
    return redirect( 'employee-list')
