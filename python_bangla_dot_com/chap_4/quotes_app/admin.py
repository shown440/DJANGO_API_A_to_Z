from django.contrib import admin

from . models import QuoteCategory
from . models import Quote

# Register your models here.
admin.site.register(QuoteCategory)
admin.site.register(Quote)
