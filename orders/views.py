from django.http import JsonResponse
from .models import ProductInCart
from django.shortcuts import render


def cart_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)
    data = request.POST
    product_id = data.get('product_id')
    nbr = data.get('nbr')
    is_delete = data.get("is_delete")

    if is_delete == 'true':
        ProductInCart.objects.filter(id=product_id).update(is_active=False)

    else:
        new_product, created = ProductInCart.objects.get_or_create(product_id=product_id, session_key=session_key,
                                                                   is_active=True, defaults={"number": nbr})
        if not created:
            new_product.number += int(nbr)
            new_product.save(force_update=True)

    # common code for two cases
    products_in_cart = ProductInCart.objects.filter(session_key=session_key, is_active=True)
    products_total_nbr = products_in_cart.count()
    return_dict['products_total_nbr'] = products_total_nbr
    return_dict['products'] = list()
    for item in products_in_cart:
        product_dict = dict()
        product_dict['id'] = item.id
        product_dict['name'] = item.product.name
        product_dict['price_per_item'] = item.price_per_item
        product_dict['nbr'] = item.number
        return_dict['products'].append(product_dict)

    return JsonResponse(return_dict)

def checkout(request):
    return render(request, 'orders/checkout.html', locals())