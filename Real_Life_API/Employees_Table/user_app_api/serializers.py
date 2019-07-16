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