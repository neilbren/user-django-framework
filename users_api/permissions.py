from rest_framework import permissions


class UpdateUser(permissions.BasePermission):

    # Bool function to determine Authentication
    def has_object_permission(self, request, view, obj):

       if request.user.is_superuser :
            return True

       elif request.method in permissions.SAFE_METHODS:
            return True
