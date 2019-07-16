from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register("hello-viewset", views.HelloViewSet, base_name="hello-viewset")

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
    # path('', QuoteCategoryAPIView.as_view(), name="couteCategoryAPI"),
]
