from django import template

from cart.cart import Cart

register = template.Library()


@register.inclusion_tag('shop/tags/pagination_numbers.html')
def show_pagination_numbers(page):
    if page.number > 3 and page.paginator.num_pages > 5 and page.number+2 < page.paginator.num_pages:
        numbers = [i for i in range(page.number-2, page.number+3)]
    elif page.number < 5:
        numbers = [i for i in range(1, min(page.paginator.num_pages+1, 6))]
    else:
        numbers = [i for i in range(page.paginator.num_pages-4, page.paginator.num_pages+1)]
    return {'numbers': numbers, 'active': page.number}


@register.simple_tag
def show_count_product_in_cart(request):
    return len(Cart(request))