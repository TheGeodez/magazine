from django.db import models


class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    def __str__(self):
        return "Пользователь %s | адрес почты: %s" % (self.name,self.email)

    class Meta:
        verbose_name = 'My subscriber'
        verbose_name_plural = 'A lot of subscribers'
