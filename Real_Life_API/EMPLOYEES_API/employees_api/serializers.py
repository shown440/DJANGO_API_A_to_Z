from rest_framework import serializers

from . import models



#########################################################################################################
###     Serializer for Admin user management (Table)
#########################################################################################################

class UserProfileSerializer(serializers.ModelSerializer):
    """ serializers.ModelSerializer imported from django rest_framework. """
    """ A serializer for our user profile objects. """

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}   #, 'name': {'write_only': True} = for hide name also

    def create(self, validated_data):
        """ Create and return a new User. """

        user = models.UserProfile(
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user



#########################################################################################################
###     Serializer for Employees Details (Table) 
#########################################################################################################

class EmployeeSerializer(serializers.ModelSerializer):
    """ serializers.ModelSerializer imported from django rest_framework. """
    """ A serializer for our Employee objects to make it JSON data. """

    class Meta:
        model = models.Employee
        fields = ('id', 'ename', 'job', 'mgr', 'date_of_birth', 'sal', 'comm', 'deptno')

    def create(self, validated_data):
        """ Create and return a new User. """

        user = models.Employee(
            ename = validated_data['ename'],
            job = validated_data['job'],
            mgr = validated_data['mgr'],
            date_of_birth = validated_data['date_of_birth'],
            sal = validated_data['sal'],
            comm = validated_data['comm'],
            deptno = validated_data['deptno']

        )

        user.save()

        return user