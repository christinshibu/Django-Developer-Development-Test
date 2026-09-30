from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Product, Category, LOW_STOCK_LIMIT
from .forms import ProductForm


@login_required
def dashboard(request):
    context = {
        'total_products': Product.objects.count(),
        'active_products': Product.objects.filter(status='active').count(),
        'inactive_products': Product.objects.filter(status='inactive').count(),
        'low_stock_products': Product.objects.filter(stock__lte=LOW_STOCK_LIMIT).count(),
    }
    return render(request, 'dashboard.html', context)


@login_required
def product_list(request):
    products = Product.objects.select_related('category').order_by('-created_at', '-id')

    # read the filters from the url
    search = request.GET.get('q', '').strip()
    category_id = request.GET.get('category', '')
    status = request.GET.get('status', '')

    if search:
        products = products.filter(name__icontains=search)
    if category_id.isdigit():
        products = products.filter(category_id=category_id)
    if status:
        products = products.filter(status=status)

    # pagination - 5 products per page
    paginator = Paginator(products, 5)
    page_obj = paginator.get_page(request.GET.get('page'))

    # keep the search/filters in the page links (everything except "page")
    params = request.GET.copy()
    params.pop('page', None)

    context = {
        'page_obj': page_obj,
        'categories': Category.objects.all(),
        'search': search,
        'selected_category': category_id,
        'selected_status': status,
        'extra_query': params.urlencode(),
        'low_stock_limit': LOW_STOCK_LIMIT,
    }
    return render(request, 'product_list.html', context)


@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})


# one view for both Add and Edit
# Add  -> pk is None
# Edit -> pk is the product id
@login_required
def product_form(request, pk=None):
    if pk:
        product = get_object_or_404(Product, pk=pk)
    else:
        product = None

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            if product:
                messages.success(request, 'Product updated successfully.')
            else:
                messages.success(request, 'Product added successfully.')
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'product_form.html', {'form': form, 'product': product})


@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    # the product is only deleted after the user confirms (POST)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted.')
        return redirect('product_list')

    return render(request, 'product_confirm_delete.html', {'product': product})
