from django.urls import path

from .views import QuoteAPIView
from .views import QuoteCategoryAPIView
from .views import QuoteAPINewView
from .views import QuoteAPIDetailView


urlpatterns = [
    path('', QuoteCategoryAPIView.as_view(), name="couteCategoryAPI"),
    path('quotes/', QuoteAPIView.as_view(), name="couteAPI"),
    path('quotes/new/', QuoteAPINewView.as_view(), name="couteAPINewPost"),
    path('quotes/<int:pk>/', QuoteAPIDetailView.as_view(), name="couteAPIDetail"),

]
