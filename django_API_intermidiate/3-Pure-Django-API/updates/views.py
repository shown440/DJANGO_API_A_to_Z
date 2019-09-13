from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.core.serializers import serialize

from django.views.generic import View

from cfeapi_project.mixins import JsonResponseMixin

from .models import Update

import json

# Create your views here.

# def detail_view(request):
#     return render(request, template, {context_dictionary})     # response JSON data
#     return HttpResponse(get_template().render({}))

#############    both works as same     ##############
def json_example_view(request):
    """ URI --- for REST API """

    data = {
        "count": 1000,
        "content": "Some new content"
    }

    return JsonResponse(data)

# def json_example_view(request):
#     """ URI --- for REST API """

#     data = {
#         "count": 1000,
#         "content": "Some new content"
#     }
#     json_data = json.dumps(data)
#     return HttpResponse(json_data, content_type='application/json')
########################################################

class JsonCBV(View):
    
    def get(self, request, *args, **kwargs):
        data = {
        "count": 1000,
        "content": "Some new content"
        }

        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):

        data = {
        "count": 1000,
        "content": "Some new content"
        }

        return self.render_to_json_response(data)


class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):

        obj = Update.objects.get(id=1)
        data = serialize("json", [obj, ], fields=('user', 'content'))

        # data = {
        # "count": obj.user.username,
        # "content": obj.content
        # }
        # json_data = json.dumps(data)
        return HttpResponse(data, content_type='application/json')


class SerializedListView(View):
    def get(self, request, *args, **kwargs):

        qs = Update.objects.all()
        data = serialize("json", qs, fields=('user', 'content'))
        print(data)

        # data = {
        # "count": obj.user.username,
        # "content": obj.content
        # }
        # json_data = json.dumps(data)
        return HttpResponse(data, content_type='application/json')