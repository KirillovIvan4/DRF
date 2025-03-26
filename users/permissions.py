from rest_framework import  permissions


class IsModer(permissions.BasePermission):

    def has_permission(self,request, view):
        return request.user.groups.filter(name="moderator").exists()

class IsNotModer(permissions.BasePermission):

    def has_permission(self,request, view):
        return not request.user.groups.filter(name="moderator").exists()

class IsCreator(permissions.BasePermission):
    def has_odject_permission(self, request, view, odj):
        if odj.creator == request.user:
            return True
        return False
