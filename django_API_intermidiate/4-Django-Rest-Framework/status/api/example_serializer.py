""" 
this is example file of Serializer only.
Video/ Lesson 29 ==> I got it 
"""

from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParsers

from .serializers import StatusSerializer
from ..models import Status


"""
Serialize Single Object
"""
obj = Status.objects.first()
print(obj)
Serializer = StatusSerializer(obj)
