from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from children.models import Children
from django.db.models import Count
from django.contrib.auth import logout


@login_required(login_url='login')
def main_page(request):
    if request.user.role == 'parents':
        return redirect('weekly_menu')  
    elif request.user.role in ['admin', 'manager', 'cooker']:
        return render(request, 'index.html') 
    else:
        return redirect('login') 
    

def dashboard(request):
    age_data = (
            Children.objects
            .values('age')
            .annotate(count=Count('id'))
            .order_by('age')
        )

    labels = [entry['age'] for entry in age_data]
    data = [entry['count'] for entry in age_data]

    context = {
            'labels': labels,  
            'data': data,      
        }
    return render(request, 'dashboard.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')