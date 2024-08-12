from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsPublicOrAdmin(BasePermission):
    """
    Позволяет доступ только к публичным объектам или администраторам.
    """

    def has_object_permission(self, request, view, obj):
        if obj.public:
            return True
        return request.user and request.user.is_staff


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        return False
