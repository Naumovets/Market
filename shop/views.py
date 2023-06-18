from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm
from shop.models import Category, Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug)
        products = products.filter(category=category)

    paginator = Paginator(products, 6)
    page_number = request.GET.get('page', 1)
    products = paginator.page(page_number)

    return render(request, 'shop/product/shop.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products})


def about(request):
    return render(request, 'shop/about.html')


def product_detail(request, id, slug):
    cart_product_form = CartAddProductForm()

    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request, 'shop/product/shop-single.html', {'product': product,
                                                             'cart_product_form': cart_product_form})


def home(request):
    return render(request, 'shop/home.html')
