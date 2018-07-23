from rest_framework.permissions import BasePermission


class IsStaff(BasePermission):
    message = "You are not Staff. Go away! You're naughty..."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return False


class IsStaffAndOwner(BasePermission):
    message = "You are not Staff or the Owner. Go away! You're naughty..."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user == obj.owner:
            return True
        return False