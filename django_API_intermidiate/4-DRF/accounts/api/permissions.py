from rest_framework import permissions

from django.contrib.auth.models import User, Permission
from django.contrib.auth import models

from django.contrib import auth
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand




class BlacklistPermission(permissions.BasePermission):
    """
    Global permission check for blacklisted IPs.
    """

    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
        return not blacklisted


class AnonPermissionOnly(permissions.BasePermission):
    message = "You are already authenticated. please logout to try again."
    """
    Anonymus / Non-Authenticated Users Only.
    """

    def has_permission(self, request, view):
        return not request.user.is_authenticated


class IsOwnerOrReadOnly(permissions.BasePermission, BaseCommand):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    # mypermissions = Permission.objects.filter(user=request.user)
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Instance must have an attribute named `owner`.
        return (obj.owner == request.user)  # or request.user.is_superuser


class RequesterPermissionList(permissions.BasePermission, BaseCommand):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    # mypermissions = Permission.objects.filter(user=request.user)
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        #################################################################################
        # user = User.objects.filter(username__iexact=request.user.username)
        user_id = User.objects.get(username__iexact=request.user.username).pk
        # permission_ids = User.user_permissions.get(USER_ID__iexact=user_id).PERMISSION_ID
        # m_permission = Permission.objects.filter(id__iexact=user_id)
        # m_per = request.user_permissions
        # print(dir(models))
        # print(permission_ids)
        
        #################################################################################
        m_permissions = set()

        # We create (but not persist) a temporary superuser and use it to game the
        # system and pull all permissions easily.
        tmp_superuser = get_user_model()(
        id=user_id
        )

        # We go over each AUTHENTICATION_BACKEND and try to fetch
        # a list of permissions
        for backend in auth.get_backends():
            if hasattr(backend, "get_all_permissions"):
                m_permissions.update(backend.get_all_permissions(tmp_superuser))

        # Make an unique list of permissions sorted by permission name.
        sorted_list_of_permissions = sorted(list(m_permissions))

        # Send a joined list of permissions to a command-line output.
        print('\n'.join(sorted_list_of_permissions))
        # print(sorted_list_of_permissions)

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user or request.user.is_superuser