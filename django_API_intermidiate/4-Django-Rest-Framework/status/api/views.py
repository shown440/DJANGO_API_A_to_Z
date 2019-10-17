from rest_framework import generics

# from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

# Custom models
from status.models import Status
from .serializers import StatusSerializer


# Create your views here.

class StatusListSearchAPIView(APIView):
    permission_classes          = []
    authentication_classes      = []

    def get(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)


class StatusAPIView(generics.ListAPIView):
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

class StatusCreateAPIView(generics.CreateAPIView):
    permission_classes          = []
    authentication_classes      = []

    queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

class StatusDetailAPIView(generics.RetrieveAPIView):
    permission_classes          = []
    authentication_classes      = []

    queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer
    # lookup_field                = "id" # "id" or "slug" #    if we want "id" or "slug" in url of urls.py

    # This fun is also alternative id lookup_field
    # def get_object(self, *args, **kwargs):
    #     kwargs = self.kwargs
    #     kw_id = kwargs.get('id')
    #     return Status.objects.get(id=kw_id)



# class StatusCreateView(generics.ListAPIView):
#     permission_classes          = []
#     authentication_classes      = []

#     queryset                    = Status.objects.all()
#     form_class                  = StatusForm


# class StatusCreateAPIView():
#     pass

# class StatusDetailAPIView():
#     pass

# class StatusUpdateAPIView():
#     pass

# class StatusDeleteAPIView():
#     pass