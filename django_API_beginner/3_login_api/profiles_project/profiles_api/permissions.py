# permissions module contains all of the base permission classes of django rest_framework
from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ Allow users to edit their own profile. """

    def has_object_permission(self, request, view, obj):
        """ Check user is trying to edit their own profile ? """

        if request.method in permissions.SAFE_METHODS:
            return True

        # obj.id = profile id AND request.user.id = id is requested from user
        return obj.id == request.user.id
       
