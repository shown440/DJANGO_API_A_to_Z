from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

# status = is used to retrive ststus code like 404, 200 500 etc.
from rest_framework import status
# TokenAuthentication is used for user is authenticate or not
from rest_framework.authentication import TokenAuthentication
# filters = is used for filtering any object. here we used it for search a profile by user name or email.
from rest_framework import filters

#import for login. rest_framework have built-in AuthTokenSerializer and ObtainAuthToken to control user login
# But those are API View so we can't say it ViewSet. So have to apply a Trick to understand system that is ViewSet.
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

# This import means that User can do anything if he is authenticated otherwise ReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# This import means that Only Authenticates User can see other profiles
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models
from . import permissions



# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handles creating, reading and Updating profiles. """

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    # Here we set authentication and permission for this ViewSet
    authentication_classes = (TokenAuthentication,)     # also add Session Authentication 
    permission_classes = (permissions.UpdateOwnProfile,)

    # here we delcare class_variable to filter profile. 1st we will declare filter type and 2nd is filter by field.
    filter_backends = (filters.SearchFilter,)   # for Search filtering
    search_fields = ('name', 'email',)  # for filtering by 'name' and 'email' fields



class LoginViewSet(viewsets.ViewSet):
    """ Check email and password and returns an auth token. """

    # set AuthTokenSerializer to the serializer_class
    serializer_class = AuthTokenSerializer

    def create(self, request):
        """ Use the ObtainAuthToken APIView to validate and create/POST a token. """

        # Now we need to do a POST request through to the ObtainAuthToken APIView and call the POST function So
            # it return ObtainAuthToken().post(request)

        return ObtainAuthToken().post(request)



class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """ Handles creating, reading and updating profile feed items. """

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer

    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)
    # permission_classes = (permissions.PostOwnStatus, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        """ Sets the user profile to the logged in user. """

        serializer.save(user_profile=self.request.user)
    




    