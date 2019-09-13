
from django.urls import path


from .views import json_example_view, JsonCBV, JsonCBV2, SerializedListView, SerializedDetailView

urlpatterns = [
    path('json/cbv/', JsonCBV.as_view()),
    path('json/cbv2/', JsonCBV2.as_view()),

    path('json/example/', json_example_view),

    path('json/serialized/detail/', SerializedDetailView.as_view()),
    path('json/serialized/list/', SerializedListView.as_view()),
    
]
