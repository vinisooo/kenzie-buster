from rest_framework import permissions
from rest_framework.views import Request, View


class MoviesPermission(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        if request.method == "POST" or request.method == "DELETE":
            return request.user.is_employee

        return request.method in permissions.SAFE_METHODS
