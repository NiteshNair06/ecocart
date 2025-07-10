from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.core.exceptions import PermissionDenied

def search_product(request):
    query = request.GET.get('q')
    products = []
    alternatives = []
    main_product = None

    if query:
        products = Product.objects.filter(Q(barcode=query) | Q(name__icontains=query))
        if products:
            main_product = products.order_by('eco_rating').first()
            category = main_product.category
            eco_rating = main_product.eco_rating
            alternatives = Product.objects.filter(
                category=category,
                eco_rating__gt=eco_rating
            ).exclude(id=main_product.id).order_by('-eco_rating')[:3]

    return render(request, 'products/search.html', {
        'products': products,
        'alternatives': alternatives,
        'main_product': main_product
    })

@login_required
@user_passes_test(lambda u: u.is_staff)
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "✅ Product added successfully!")
                return redirect('search')
            except:
                messages.error(request, "⚠️ Product with this barcode already exists.")
        else:
            messages.error(request, "⚠️ Please check the fields.")
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})

@login_required
# @user_passes_test(lambda u: u.is_staff)
def edit_product(request, pk):

    if not request.user.is_staff:
        raise PermissionDenied()  # 👈 This will show your 403.html

    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Product updated successfully!")
            return redirect('search')
        else:
            messages.error(request, "⚠️ Error updating product.")
    else:
        form = ProductForm(instance=product)

    return render(request, 'products/edit_product.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, "🗑️ Product deleted successfully!")
        return redirect('search')

    return render(request, 'products/confirm_delete.html', {'product': product})
