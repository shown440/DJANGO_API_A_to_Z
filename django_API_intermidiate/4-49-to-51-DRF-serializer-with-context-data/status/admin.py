from django.contrib import admin
from .models import Status
from .forms import StatusForm


class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', '__str__', 'image'] # __str__ = content | bcz in model we return content in __str__ method
    
    form = StatusForm
    class Meta:
        model = Status


# Register your models here.
admin.site.register(Status, StatusAdmin)