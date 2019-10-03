# Builtin models
from django.views.generic import View
from django.http import HttpResponse
## For serialize data
from django.core.serializers import serialize

# Custom models
from updates.models import Update as UpdateModel


# Retriving(1), Creating, Updating, Deleting: Model--> 'Update'
class UpdateModelDetailAPIView(View):
    """ Retrive, Update and Delete """

    def get(self, request, id, *args, **kwargs):

        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()

        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):

        json_data = {}

        return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):

        json_data = {}

        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):

        json_data = {}

        return HttpResponse(json_data, content_type='application/json')


# Retriving All: Model--> 'Update'
class UpdateModelListAPIView(View):
    """ List, Create """

    def get(self, request, *args, **kwargs):

        qs = UpdateModel.objects.all()
        # qs = Update.objects.filter(id__gte=2) --> For Filtering
        json_data = qs.serialize()

        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):

        json_data = {}

        return HttpResponse(json_data, content_type='application/json')