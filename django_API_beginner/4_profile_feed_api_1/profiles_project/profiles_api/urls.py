from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()

# when we are registering model view set, then no need to specify base_name. django restframewok 
# automatically do this by looking model which is registered with serializer and our viewset.
router.register("profile", views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

router.register('login', views.LoginViewSet, base_name='login')


urlpatterns = [
    # path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
    # path('', QuoteCategoryAPIView.as_view(), name="couteCategoryAPI"),
]
