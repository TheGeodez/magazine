from django.shortcuts import render
from .forms import SubscriberForm
from products.models import ProductImage

def landing(request):
    form = SubscriberForm(request.POST or None)
    if request.method == 'POST':
        form.save()
    return render(request, 'landing/landing.html', locals())

def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__category__is_active=True)
    products_images_phones = products_images.filter(product__category__id = 1)
    products_images_laptops = products_images.filter(product__category__id = 2)
    return render(request, 'landing/home.html', locals())
