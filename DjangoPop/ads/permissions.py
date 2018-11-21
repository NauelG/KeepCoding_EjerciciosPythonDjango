from rest_framework.permissions import BasePermission


class AdPermission(BasePermission):

    def has_permission(self, request, view):
        # Define si el usuario autenticado puede realizar la accion
        return request.user.is_authenticated or request.method == 'GET'

    def has_object_permission(self, request, view, obj):
        # Define si el usuario autenticado puede realizar la accion sobre el objeto obj
        return view.action == 'retrieve' or obj.owner == request.user or request.user.is_superuser