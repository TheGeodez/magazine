from django.db import models
from products.models import Product


class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Статус %s" % self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы заказов'


class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    customer_name = models.CharField(max_length=128, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=128, blank=True, null=True, default=None)
    adress = models.CharField(max_length=60, blank=True, null=True, default=None)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return 'Заказ %s %s' % (self.id, self.status.name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    number = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    def __str__(self):
        return '%s' % self.product.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
