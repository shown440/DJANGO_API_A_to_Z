# Builtin Library
from django.views.generic import View
from django.http import HttpResponse
import json
## For serialize data
from django.core.serializers import serialize

# Custom models
from updates.models import Update as UpdateModel

# Custom Forms
from updates.forms import UpdateModelForm

# Custom Mixins
## import mixin for csrf token
from .mixins import CSRFExemptionMixin
## from cfeapi_project.mixins import HttpResponse for Response from UpdateModelListAPIView
from cfeapi_project.mixins import HttpResponseMixin


# Retriving(1), Creating, Updating, Deleting: Model--> 'Update'
class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExemptionMixin, View):
    """ Retrive, Update and Delete """

    is_json=True

    def get(self, request, id, *args, **kwargs):

        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()

        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):

        json_data = json.dumps({"message": "Not allowed, please use the /api/updates endpoint"})

        return self.render_to_response(json_data, status=403)

    def put(self, request, *args, **kwargs):

        json_data = {}

        return self.render_to_response(json_data)

    def delete(self, request, *args, **kwargs):

        json_data = {}

        return self.render_to_response(json_data, status=403)


# Retriving All: Model--> 'Update'
class UpdateModelListAPIView(HttpResponseMixin, CSRFExemptionMixin, View):
    """ List, Create """

    is_json=True
    # def render_to_response(data, status=200):
    #     return HttpResponse(data, content_type='application/json', status=status)

    def get(self, request, *args, **kwargs):

        qs = UpdateModel.objects.all()
        # qs = Update.objects.filter(id__gte=2) --> For Filtering
        json_data = qs.serialize()
        return self.render_to_response(json_data)


    def post(self, request, *args, **kwargs):

        # print(request.POST)
        form = UpdateModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=201)
        
        json_data = json.dumps({"message": "Not Allowed"})
        return self.render_to_response(json_data, status=400)


    def delete(self, request, *args, **kwargs):

        json_data = json.dumps({"message": "You can't delete entire List"})
        status_code = 403 # Not Allowed/ Forbidden
        return self.render_to_response(json_data, status=403)