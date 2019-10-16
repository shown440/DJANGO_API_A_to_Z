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

# Custom JSON data validator
from .utils import is_json


# Retriving(1), Creating, Updating, Deleting: Model--> 'Update'
class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExemptionMixin, View):
    """ 
        Retrive ---> 1/Single object, 
        Update and 
        Delete 
    """

    is_json=True

    def get_object(self, id=None):
        # try:
        #     obj = UpdateModel.objects.get(id=id)
        # except UpdateModel.DoesNotExist:
        #     obj = None
        # return obj
        """ Both code are same (Upper and Lower) """
        qs = UpdateModel.objects.filter(id=id)
        if qs.count() == 1 :
            return qs.first()
        return None

    def get(self, request, id, *args, **kwargs):
        # Object Validation
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Retrive data does not found. Wrong ID"})
            return self.render_to_response(error_data, status=404)

        json_data = obj.serialize()
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):

        json_data = json.dumps({"message": "Not allowed, please use the /api/updates endpoint"})

        return self.render_to_response(json_data, status=403)

    def put(self, request, id, *args, **kwargs):
        # JSON data validation checking
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message": "Update/PUT data format is Not JSON. Please send JSON data."})
            return self.render_to_response(error_data, status=400)
        # Object Validation   
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Update data does not found. Wrong ID"})
            return self.render_to_response(error_data, status=404)

        # data is our Original Serialize data from model.py--> class Update--> def serialize
        data = json.loads(obj.serialize())
        # print(data)
        # passed_data is sent by client
        passed_data = json.loads(request.body)
        # add passed_data into data for serialize using for loop 
        for key, value in passed_data.items():
            data[key] = value
        # print(data)
        # print(passed_data)
        form = UpdateModelForm(data, instance=obj)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = json.dumps(data)
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        
        # print(dir(request))
        print(request.body)
        # new_data = json.loads(request.body)
        # print(new_data['content']) # ['content']


        json_data = json.dumps({"message": "Returns from PUT method"})
        return self.render_to_response(json_data)

    def delete(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Delete data does not found. Wrong ID"})
            return self.render_to_response(error_data, status=404)

        deleted_, item_deleted = obj.delete()
        print(deleted_, "========> ", item_deleted)
        if deleted_ == 1:
            json_data = json.dumps({"message": "Successfully Deleted. Returns from DELETE method"})        
            return self.render_to_response(json_data, status=200)
        error_data = json.dumps({"message": "Couldn't delete item. try later."})
        return self.render_to_response(error_data, status=400)


# AUTH / Permissions -- DJANGO REST FRAMEWORK -- DONT USE Tastypie


# /api/updates/ 
# Retriving All: Model--> 'Update'
class UpdateModelListAPIView(HttpResponseMixin, CSRFExemptionMixin, View):
    """ 
        List view ---> Retrive list,
        Create
        Update and
        Delete
    """

    is_json=True
    queryset = None

    def get_queryset(self):
        qs = UpdateModel.objects.all()
        self.queryset = qs
        return self.queryset
    
    def get_object(self, id=None):
        # try:
        #     obj = UpdateModel.objects.get(id=id)
        # except UpdateModel.DoesNotExist:
        #     obj = None
        # return obj
        """ Both code are same (Upper and Lower) """
        if id is None:
            return None
        qs = self.get_queryset().filter(id=id)   # UpdateModel.objects.filter(id=id)
        if qs.count() == 1 :
            return qs.first()
        return None

    # def render_to_response(data, status=200):
    #     return HttpResponse(data, content_type='application/json', status=status)

    def get(self, request, *args, **kwargs):
        data = json.loads(request.body)
        print(data)
        passed_id = data.get('id', None)

        if passed_id is not None:
            # Object Validation
            obj = self.get_object(id=passed_id)
            if obj is None:
                error_data = json.dumps({"message": "Retrive data does not found. Wrong ID"})
                return self.render_to_response(error_data, status=404)
            json_data = obj.serialize()
            return self.render_to_response(json_data)
        else:
            qs = self.get_queryset() # UpdateModel.objects.all()
            # qs = Update.objects.filter(id__gte=2) --> For Filtering
            json_data = qs.serialize()
            return self.render_to_response(json_data)


    def post(self, request, *args, **kwargs):

        # JSON data validation checking
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message": "Create/POST data format is Not JSON. Please send JSON data."})
            return self.render_to_response(error_data, status=400)

        # print(request.POST)
        data = json.loads(request.body)
        form = UpdateModelForm(data)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        
        json_data = json.dumps({"message": "Not Allowed"})
        return self.render_to_response(json_data, status=400)


    # def delete(self, request, *args, **kwargs):
        
    #     json_data = json.dumps({"message": "You can't delete entire List"})
    #     status_code = 403 # Not Allowed/ Forbidden
    #     return self.render_to_response(json_data, status=403)

    def put(self, request, *args, **kwargs):
        # JSON data validation checking
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message": "Update/PUT data format is Not JSON. Please send JSON data."})
            return self.render_to_response(error_data, status=400)
        
        # passed_data is sent by client
        passed_data = json.loads(request.body)
        passed_id = passed_data.get('id', None)
        # If passed_id == None then we will tell client that 'id is required field'
        if not passed_id:
            error_data = json.dumps({"message": "ID is required fiels. Return From PUT--> UpdateModelListAPIView"})
            return self.render_to_response(error_data, status=400)

        # Object Validation   
        obj = self.get_object(id=passed_id)
        if obj is None:
            error_data = json.dumps({"message": "Object not found. Wrong ID. Return From PUT--> UpdateModelListAPIView"})
            return self.render_to_response(error_data, status=404)

        # data is our Original Serialize data from model.py--> class Update--> def serialize
        data = json.loads(obj.serialize())
        print(data)
        # add passed_data into data for serialize using for loop 
        for key, value in passed_data.items():
            data[key] = value
        # print(data)
        # print(passed_data)
        form = UpdateModelForm(data, instance=obj)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = json.dumps(data)
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        
        # print(dir(request))
        print(request.body)
        # new_data = json.loads(request.body)
        # print(new_data['content']) # ['content']


        json_data = json.dumps({"message": "Returns from PUT method"})
        return self.render_to_response(json_data)

    def delete(self, request, *args, **kwargs):
        # JSON data validation checking
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message": "Update/PUT data format is Not JSON. Please send JSON data."})
            return self.render_to_response(error_data, status=400)
        
        # passed_data is sent by client
        passed_data = json.loads(request.body)
        passed_id = passed_data.get('id', None)
        # If passed_id == None then we will tell client that 'id is required field'
        if not passed_id:
            error_data = json.dumps({"message": "ID is required fiels. Return From DELETE--> UpdateModelListAPIView"})
            return self.render_to_response(error_data, status=400)

        # Object Validation   
        obj = self.get_object(id=passed_id)
        if obj is None:
            error_data = json.dumps({"message": "Object not found. Wrong ID. Return From DELETE--> UpdateModelListAPIView"})
            return self.render_to_response(error_data, status=404)


        deleted_, item_deleted = obj.delete()
        print(deleted_, "========> ", item_deleted)
        if deleted_ == 1:
            json_data = json.dumps({"message": "Successfully Deleted. Returns from DELETE method"})        
            return self.render_to_response(json_data, status=200)
        error_data = json.dumps({"message": "Couldn't delete item. try later."})
        return self.render_to_response(error_data, status=400)