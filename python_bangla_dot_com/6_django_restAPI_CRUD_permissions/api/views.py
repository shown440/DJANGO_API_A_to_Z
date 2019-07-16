from django.shortcuts import render

# import django rest framework
# permissions = use for authentication in view level
from rest_framework import generics, permissions

# import Quote, QuoteCategory from quotes_app.models
from quotes_app.models import Quote
from quotes_app.models import QuoteCategory

# import QuoteSerializer, QuoteCategorySerializer from api.serializers
from .serializers import QuoteSerializer
from .serializers import QuoteCategorySerializer


# Create your views here.

class QuoteAPIView(generics.ListAPIView):
    #permission_classes = (permissions.IsAuthenticated, )
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class QuoteCategoryAPIView(generics.ListAPIView):
    queryset = QuoteCategory.objects.all()
    serializer_class = QuoteCategorySerializer


class QuoteAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class QuoteAPINewView(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated, )
    queryset = Quote.objects.all().order_by('-id')[:1] # Latest Quote
    serializer_class = QuoteSerializer
