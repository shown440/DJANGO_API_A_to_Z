from django.shortcuts import render

from rest_framework import viewsets

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
###from . import permissions

# Create your views here.


#####################################################################################################
###     ViewSet for Employees Details
#####################################################################################################

""" This class is ViewSet for view Employees. """
class EmployeeViewSet(viewsets.ModelViewSet):
    """ Handles creating, reading and Updating profiles. """

    serializer_class = serializers.EmployeeSerializer
    queryset = models.Employee.objects.all()

    # Here we set authentication and permission for this ViewSet
    ###authentication_classes = (TokenAuthentication,)     # also add Session Authentication 
    permission_classes = (IsAuthenticatedOrReadOnly,)    #permissions.UpdateOwnProfile

    # here we delcare class_variable to filter profile. 1st we will declare filter type and 2nd is filter by field.
    filter_backends = (filters.SearchFilter,)   # for Search filtering
    search_fields = ('id', 'employee_name', 'date_of_birth',)  # for filtering by 'name' and 'email' fields



#####################################################################################################
###     ViewSet for Department Details
#####################################################################################################

""" This class is ViewSet for view Employees. """
class DepartmentViewSet(viewsets.ModelViewSet):
    """ Handles creating, reading and Updating profiles. """

    serializer_class = serializers.DepartmentSerializer
    queryset = models.Department.objects.all()

    # Here we set authentication and permission for this ViewSet
    ###authentication_classes = (TokenAuthentication,)     # also add Session Authentication 
    permission_classes = (IsAuthenticatedOrReadOnly,)    #permissions.UpdateOwnProfile

    # here we delcare class_variable to filter profile. 1st we will declare filter type and 2nd is filter by field.
    filter_backends = (filters.SearchFilter,)   # for Search filtering
    search_fields = ('department_no', 'department_name', )  # for filtering by 'name' and 'email' fields