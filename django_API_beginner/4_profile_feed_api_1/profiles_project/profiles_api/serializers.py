from rest_framework import serializers

from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    """ serializers.ModelSerializer imported from django rest_framework. """
    """ A serializer for our user profile objects. """

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}   #, 'name': {'write_only': True} = for hide name also

    def create(self, validated_data):
        """ Create and return a new User. """

        user = models.UserProfile(
            email = validated_data['email'],
            name = validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """ A serializer for profile feed items. """

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {"read_only": True}}
        

    # def create(self, validated_data):
    #     """ Create and return a new User. """

    #     feed = models.ProfileFeedItem(
    #         #user_profile = validated_data['user_profile'],
    #         status_text = validated_data['status_text']
    #     )

    #     feed.save()

    #     return feed
        


