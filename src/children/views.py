from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.models import Group
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model
from django.utils.dateparse import parse_datetime
from .forms import ChildForm, GroupForm
from .models import Children, ChildGroup
from django.contrib.auth.decorators import login_required
from django.utils import timezone


Users = get_user_model()

@login_required(login_url='login')
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

    return render(request, 'children_rg.html', {'form': form})



@login_required(login_url='login')
def registration_history(request):
    children = Children.objects.select_related('parent').order_by('-id')
    ctx = {
        "children":children,
    }
    return render(request, 'children_list.html', ctx)




@login_required(login_url='login')
def edit_child(request, pk):
    child = get_object_or_404(Children, pk=pk)
    parent = child.parent

    if request.method == 'POST':
        child.name = request.POST.get('name')
        child.age = request.POST.get('age')
        new_email = request.POST.get('email')
        new_password = request.POST.get('password')
        created = request.POST.get('created')

        if new_email:
            parent.email = new_email
            parent.save()
        if new_password:
            parent.set_password(new_password)
            parent.save()
            child.raw_password = new_password

        if created:
            child.created = parse_datetime(created)

        child.save()
        return redirect('children_list')

    return render(request, 'edit_child.html', {'child': child})


@login_required(login_url='login')
def child_delete(request, pk):
    child = get_object_or_404(Children, pk=pk)
    child.delete()
    return redirect('children_list')


@login_required(login_url='login')
def group_list(request):
    groups = ChildGroup.objects.all()
    return render(request, 'group_list.html', {'groups': groups})


@login_required(login_url='login')
def add_group(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name :
            ChildGroup.objects.create(name=name)
            return redirect('group_list')
    return render(request, 'add_group.html')


@login_required(login_url='login')
def group_detail(request, group_id):
    group = get_object_or_404(ChildGroup, id=group_id)

    sort_by = request.GET.get('sort', 'default')
    if sort_by == 'age_asc':
        children = group.children.order_by('age')
    elif sort_by == 'age_desc':
        children = group.children.order_by('-age')
    else:
        children = group.children.all()

    return render(request, 'group_detail.html', {
        'group': group,
        'children': children,
        'sort_by': sort_by
    })


@login_required
def edit_group(request, pk):
    group = get_object_or_404(ChildGroup, id=pk)
    
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            group = form.save(commit=False)
            if not group.data:
                group.data = timezone.now().date()
            group.save()
            return redirect('group_list')
    else:
        form = GroupForm(instance=group)
    
    return render(request, 'edit_group.html', {'form': form})

@login_required
def delete_group(request, pk):
    group = get_object_or_404(ChildGroup, pk=pk)
    group.delete()
    return redirect( 'group_list')

