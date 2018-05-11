from django.contrib import admin
from .models import Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['id','name','email']
    list_filter = ['email']
    search_fields = ['name', 'email']

    class Meta:
        model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)
