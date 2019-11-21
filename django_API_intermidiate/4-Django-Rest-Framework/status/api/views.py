########### Mixin models portion ##########################
from rest_framework import mixins

########### View portion ##########################
# from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework import generics
from rest_framework.views import APIView
# from rest_framework.response import Response

########### Permission portion ####################
from rest_framework import permissions
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User # add, change, delete, view

########### Authentication portion ################
from rest_framework.authentication import SessionAuthentication

from django.shortcuts import get_object_or_404
import json 

# Custom models
from status.models import Status
from .serializers import StatusSerializer

################################################################
### Check is_json or not
################################################################
def is_json(json_data):
    try:
        real_data = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid

# CreateModelMixin ---- used for Handelling     POST data
# RetrieveModelMixin --- used for Handelling     GET data
# UpdateModelMixin ---- used for Handelling     PUT data
# DestroyModelMixin ---- used for Handelling    DELETE data

# @permission_required
# user = get_object_or_404(User, pk=user.id)
# @user.has_perm('status.delete_Status')
class StatusAPIDetailView(mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.RetrieveAPIView):
    permission_classes          = [permissions.IsAuthenticated]     #[ IsAuthenticated, IsAuthenticatedOrReadOnly ]
    authentication_classes      = [SessionAuthentication]

    # queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer
    queryset                    = Status.objects.all()
    # lookup_field                = "id"

    # @permission_required
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # @permission_required
    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    # @permission_required
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


# @permission_required
class StatusAPIView(mixins.CreateModelMixin,
                    # mixins.RetrieveModelMixin,
                    # mixins.UpdateModelMixin,
                    # mixins.DestroyModelMixin,  
                    generics.ListAPIView):
    permission_classes          = [permissions.IsAuthenticated]     #[ IsAuthenticated, IsAuthenticatedOrReadOnly ]
    authentication_classes      = [SessionAuthentication]

    # queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer
    passed_id                   = None

    def get_queryset(self):
        request     = self.request
        print(request.user)
        qs          = Status.objects.all()
        query       = request.GET.get('q')
        # print("$$$$$$$$$$$$$$$$$$$$$$> ",query)
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs 
    # @permission_required
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    # @permission_required
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# class StatusAPIView(mixins.CreateModelMixin,
#                     mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,  
#                     generics.ListAPIView):
#     permission_classes          = []
#     authentication_classes      = []

#     # queryset                    = Status.objects.all()
#     serializer_class            = StatusSerializer
#     passed_id                   = None

#     def get_queryset(self):
#         request     = self.request
#         qs          = Status.objects.all()
#         query       = request.GET.get('q')
#         # print("$$$$$$$$$$$$$$$$$$$$$$> ",query)
#         if query is not None:
#             qs = qs.filter(content__icontains=query)
#         return qs 

#     def get_object(self):
#         request             = self.request
#         passed_id           = request.GET.get('id', None) or self.passed_id
#         queryset            = self.get_queryset()
#         obj                 = None

#         if passed_id is not None:
#             obj             = get_object_or_404(queryset, id=passed_id)
#             self.check_object_permissions(request, obj)
#         return obj

#     # Now destroy is no need for delete
#     # def perform_destroy(self, instance):
#     #     if instance in not None:
#     #         return instance.delete()
#     #     return None


#     def get(self, request, *args, **kwargs):
#         url_passed_id           = request.GET.get('id', None)
#         json_data               = {}
#         body_                   = request.body
#         if is_json(body_):
#             json_data               = json.loads(request.body)
#         new_passed_id           = json_data.get("id", None)
#         # print(request.body)  # ==> Used for passed data using BODY
#         # request.data  # ==> Used for passed data using DATA

#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id

#         if passed_id is not None: # or passed_id is not "":
#             return self.retrieve(request, *args, **kwargs) # This retrieve method will call "def get_object(self): Method"
#         return super().get(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         url_passed_id           = request.GET.get('id', None)
#         json_data               = {}
#         body_                   = request.body
#         if is_json(body_):
#             json_data               = json.loads(request.body)
#         new_passed_id           = json_data.get("id", None)
#         # print(request.body)  # ==> Used for passed data using BODY
#         # request.data  # ==> Used for passed data using DATA
#         print(request.data)
#         requested_id = None # request.data.get('id')

#         passed_id = url_passed_id or new_passed_id or None or requested_id
#         self.passed_id = passed_id
#         return self.update(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):
#         url_passed_id           = request.GET.get('id', None)
#         json_data               = {}
#         body_                   = request.body
#         if is_json(body_):
#             json_data               = json.loads(request.body)
#         new_passed_id           = json_data.get("id", None)
#         # print(request.body)  # ==> Used for passed data using BODY
#         # request.data  # ==> Used for passed data using DATA

#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         url_passed_id           = request.GET.get('id', None)
#         json_data               = {}
#         body_                   = request.body
#         if is_json(body_):
#             json_data               = json.loads(request.body)
#         new_passed_id           = json_data.get("id", None)
#         # print(request.body)  # ==> Used for passed data using BODY
#         # request.data  # ==> Used for passed data using DATA

#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id
#         return self.destroy(request, *args, **kwargs)

#     # def perform_create(self, serializer):
#     #     serializer.save(user=self.request.user)



























# # Create your views here.

# # class StatusListSearchAPIView(APIView):
# #     permission_classes          = []
# #     authentication_classes      = []

# #     def get(self, request, format=None):
# #         qs = Status.objects.all()
# #         serializer = StatusSerializer(qs, many=True)
# #         return Response(serializer.data)

# #     def post(self, request, format=None):
# #         qs = Status.objects.all()
# #         serializer = StatusSerializer(qs, many=True)
# #         return Response(serializer.data)


# # CreateModelMixin ---- used for Handelling     POST data
# # UpdateModelMixin ---- used for Handelling     PUT data
# # DestroyModelMixin ---- used for Handelling    DELETE data

# class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView):
#     permission_classes          = []
#     authentication_classes      = []

#     # queryset                    = Status.objects.all()
#     serializer_class            = StatusSerializer

#     def get_queryset(self):
#         qs = Status.objects.all()
#         query = self.request.GET.get('q')
#         # print("$$$$$$$$$$$$$$$$$$$$$$> ",query)
#         if query is not None:
#             qs = qs.filter(content__icontains=query)
#         return qs 

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#     # def perform_create(self, serializer):
#     #     serializer.save(user=self.request.user)

# class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView): # mixins.CreateModelMixin, 
#     permission_classes          = []
#     authentication_classes      = []

#     queryset                    = Status.objects.all()
#     serializer_class            = StatusSerializer



# class StatusDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView): # mixins.CreateModelMixin, 
#     permission_classes          = []
#     authentication_classes      = []

#     queryset                    = Status.objects.all()
#     serializer_class            = StatusSerializer
#     # lookup_field                = "id" # "id" or "slug" #    if we want "id" or "slug" in url of urls.py

#     # def post(self, request, *args, **kwargs):
#     #     return self.create(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# # class StatusUpdateAPIView(generics.UpdateAPIView):
# #     permission_classes          = []
# #     authentication_classes      = []

# #     queryset                    = Status.objects.all()
# #     serializer_class            = StatusSerializer
# #     # lookup_field                = "id" # "id" or "slug" #    if we want "id" or "slug" in url of urls.py

# # class StatusDeleteAPIView(generics.DestroyAPIView):
# #     permission_classes          = []
# #     authentication_classes      = []

# #     queryset                    = Status.objects.all()
# #     serializer_class            = StatusSerializer
# #     # lookup_field                = "id" # "id" or "slug" #    if we want "id" or "slug" in url of urls.py
