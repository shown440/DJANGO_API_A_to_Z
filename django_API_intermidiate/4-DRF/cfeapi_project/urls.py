"""cfeapi_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# I'll put it into my account app -> urls.py later
from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    # URL's for JWT Authentication
    path('api/auth/', include('accounts.api.urls')),
    path('api/auth', include('accounts.api.urls')),

    # with and without end SLASH both are workable
    path('api/updates/', include('updates.api.urls')),
    path('api/updates', include('updates.api.urls')),

    path('api/status/', include('status.api.urls')),
    path('api/status', include('status.api.urls')),
]
