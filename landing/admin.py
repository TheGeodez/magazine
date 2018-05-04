from django.contrib import admin
from .models import Subscribers

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['id','name','email']
    list_filter = ['email']
    search_fields = ['name', 'email']

    class Meta:
        model = Subscribers

admin.site.register(Subscribers, SubscriberAdmin)
