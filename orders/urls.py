from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^landing/$', views.landing, name='landing'),
    url(r'^cart_adding/$', views.cart_adding, name='cart_adding'),
    url(r'^checkout/$', views.checkout, name='cart_adding'),
]
