from django.shortcuts import render,redirect
from .forms import ProductForm
from .models import Products


def adding_pr(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')  
    else:
        form = ProductForm()

    return render(request, 'addpr.html', {'form': form})

def product_list_view(request):
    products = Products.objects.all().order_by('name')
    return render(request, 'product_list.html', {'products': products})