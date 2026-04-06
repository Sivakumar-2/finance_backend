from rest_framework.permissions import BasePermission

class RecordPermission(BasePermission):

    def has_permission(self, request, view):
        user = request.user

        if not user or not hasattr(user, 'role'):
            return False

        role = user.role

        # Read access
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return role in ['viewer', 'analyst', 'admin']

        # Write access
        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return role == 'admin'

        return False

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Admin can access everything
        if user.role == 'admin':
            return True

        # Others can only access their own records
        return obj.created_by == user