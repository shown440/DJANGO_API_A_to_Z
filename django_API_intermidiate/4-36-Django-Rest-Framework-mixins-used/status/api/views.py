from rest_framework import generics, mixins

# from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

# Custom models
from status.models import Status
from .serializers import StatusSerializer


# Create your views here.

# class StatusListSearchAPIView(APIView):
#     permission_classes          = []
#     authentication_classes      = []

#     def get(self, request, format=None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)


# CreateModelMixin ---- used for Handelling     POST data
# UpdateModelMixin ---- used for Handelling     PUT data
# DestroyModelMixin ---- used for Handelling    DELETE data

class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes          = []
    authentication_classes      = []

    # queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        # print("$$$$$$$$$$$$$$$$$$$$$$> ",query)
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs 

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView): # mixins.CreateModelMixin, 
    permission_classes          = []
    authentication_classes      = []

    queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer



class StatusDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView): # mixins.CreateModelMixin, 
    permission_classes          = []
    authentication_classes      = []

    queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer
    # lookup_field                = "id" # "id" or "slug" #    if we want "id" or "slug" in url of urls.py

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# class StatusUpdateAPIView(generics.UpdateAPIView):
#     permission_classes          = []
#     authentication_classes      = []

#     queryset                    = Status.objects.all()
#     serializer_class            = StatusSerializer
#     # lookup_field                = "id" # "id" or "slug" #    if we want "id" or "slug" in url of urls.py

# class StatusDeleteAPIView(generics.DestroyAPIView):
#     permission_classes          = []
#     authentication_classes      = []

#     queryset                    = Status.objects.all()
#     serializer_class            = StatusSerializer
#     # lookup_field                = "id" # "id" or "slug" #    if we want "id" or "slug" in url of urls.py
