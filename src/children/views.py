from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model
from .forms import ChildForm
from .models import Children

Users = get_user_model()

def child_registration(request):
    parent_credentials = None

    if request.method == 'POST':
        form = ChildForm(request.POST)
        if form.is_valid():
            child = form.save(commit=False)
            parent_email = form.cleaned_data.get('parent_email')

            parent_user, created = Users.objects.get_or_create(
                email=parent_email,
                defaults={
                    'name': f"Parent of {child.name}",
                    'role': 'parents',
                    'is_active': True,
                }
            )

            if created:
                password = get_random_string(length=8)
                parent_user.set_password(password)
                child.raw_password = password
                parent_user.save()
                parent_credentials = {
                    'email': parent_user.email,
                    'password': password
                }

            child.parent = parent_user
            child.save()

            return render(request, 'children_rg.html', {
                'form': ChildForm(),
                'success': True,
                'parent_credentials': parent_credentials
            })
    else:
        form = ChildForm()

    return render(request, 'children_rg.html', {
        'form': form
    })




def registration_history(request):
    children = Children.objects.select_related('parent').order_by('-id')
    return render(request, 'children_list.html', {'children': children})