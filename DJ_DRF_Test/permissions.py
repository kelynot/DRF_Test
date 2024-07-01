from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method is permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.customuser == request.customuser


class IsCustomer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user


class IsAssignedToTask(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.assigned_to == request.user


class CanViewTask(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return not obj.assigned_to or obj.assigned_to == request.user or obj.created_by


class CanEditTask(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method is permissions.SAFE_METHODS:
            return True
        if obj.status == 'COMPLETED':
            return False
        return obj.assigned_to == request.user or request.user.has_perm('view_all_tasks')


class IsEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method is permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            role = request.user.role
            return bool(request.user and role == "employee")
        return False



