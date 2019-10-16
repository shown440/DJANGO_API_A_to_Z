""" 
this is example file of Serializer only.
Video/ Lesson 29 ==> I got it 
"""
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cfeapi_project.settings")


# from django.conf import settings

from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .serializers import StatusSerializer
from ..models import Status

# settings.configure()


"""
Serialize Single Object
"""
obj = Status.objects.first()
print(obj)
serializer = StatusSerializer(obj)
serializer.data
print(serializer.data)
json_data = JSONRenderer().render(serializer.data)
print(json_data)

steram = BytesIO(json_data)
print(steram)
data = JSONParser().parse(steram)
print(data)

"""
Serialize a QuerySet
"""
qs = Status.objects.all()
print(qs)
serializer2 = StatusSerializer(qs, many=True)
serializer2.data
print(serializer2.data)
json_data2 = JSONRenderer().render(serializer2.data)
print(json_data2)

steram2 = BytesIO(json_data2)
print(steram2)
data2 = JSONParser().parse(steram2)
print(data2)

"""
Create Obj
"""
data = {'user': 1}

serializer = StatusSerializer(data=data)
serializer.is_valid()
serializer.save()

# if serializer.is_valid():
#     serializer.save()

"""
Update Obj
"""
obj = Status.objects.first()    # id=4
data = {'content': 'Django is awesome for fullstack development.', 'user': 1}

update_serializer = StatusSerializer(obj, data=data)
update_serializer.is_valid()
update_serializer.save()
# update_serializer.errors  # to check the errors of the serializers

"""
Delete Obj
"""
data = {'user': 1, 'content': 'PWA is awesome concept for offline web application'}

create_obj_serializer = StatusSerializer(data=data)
create_obj_serializer.is_valid()
create_obj = create_obj_serializer.save()
print(create_obj)

# data = {'id': 8}
obj = Status.objects.last()    # id=4
get_data_serializer = StatusSerializer(obj)
# get_data_serializer.is_valid()
# create_obj = get_data_serializer.save()
print(get_data_serializer.data)
# print(obj.delete) # for delete the object





