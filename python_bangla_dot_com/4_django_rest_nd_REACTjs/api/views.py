from django.shortcuts import render

# import django rest framework
from rest_framework import generics

# import Quote, QuoteCategory from quotes_app.models
from quotes_app.models import Quote
from quotes_app.models import QuoteCategory

# import QuoteSerializer, QuoteCategorySerializer from api.serializers
from .serializers import QuoteSerializer
from .serializers import QuoteCategorySerializer


# Create your views here.

class QuoteAPIView(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class QuoteCategoryAPIView(generics.ListAPIView):
    queryset = QuoteCategory.objects.all()
    serializer_class = QuoteCategorySerializer
