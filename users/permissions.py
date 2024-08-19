from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj == request.user


class IsPublicOrAdmin(BasePermission):
    """
    Позволяет доступ только к публичным объектам или администраторам.
    """

    def has_object_permission(self, request, view, obj):
        if obj.public:
            return True
        return request.user and request.user.is_staff


class IsOwnerOrReadOnly(BasePermission):
    """
    Разрешает доступ только владельцам объекта,
    для всех остальных только просмотр.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in ["GET"]:
            return True
        return obj.user == request.user
