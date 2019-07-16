from django.urls import path

from .views import QuoteAPIView
from .views import QuoteCategoryAPIView


urlpatterns = [
    path('', QuoteCategoryAPIView.as_view(), name="couteCategoryAPI"),
    path('quotes/', QuoteAPIView.as_view(), name="couteAPI"),


]
