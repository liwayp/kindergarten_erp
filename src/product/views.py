from django.shortcuts import render,redirect, get_object_or_404
from .forms import ProductForm
from .models import Products
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def adding_pr(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  
    else:
        form = ProductForm()

    return render(request, 'addpr.html', {'form': form})

def product_list_view(request):
    products = Products.objects.all().order_by('name')
    return render(request, 'product_list.html', {'products': products})


@login_required(login_url='login')
def product_edit(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'editpr.html', {'form': form, 'product': product})


@login_required(login_url='login')
def product_delete(request, pk):
    product = get_object_or_404(Products, id=pk)
    product.delete()
    return redirect('product_list')

