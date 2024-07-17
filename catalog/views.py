from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'catalog/contacts.html')


def product_view(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/product_basis_form.html', context)


def product_detail(request, pk):
    # product = Product.objects.get(pk=pk)
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'catalog/product_detail.html', context)
