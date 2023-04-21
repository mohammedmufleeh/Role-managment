from rest_framework.permissions import BasePermission

class IsSuperAdminOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            member = Member.objects.filter(user=request.user).first()
            if member and member.role.name in ['Super Admin', 'Admin']:
                return True
        return False

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            member = Member.objects.filter(user=request.user).first()
            if member and member.role.name == 'Admin':
                return True
        return False

class IsOperator(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            member = Member.objects.filter(user=request.user).first()
            if member and member.role.name == 'Operator':
                return True
        return False

class IsTechnician(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            member = Member.objects.filter(user=request.user).first()
            if member and member.role.name == 'Technician':
                return True
        return False

class CanEditRole(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            member = Member.objects.filter(user=request.user).first()
            if member and obj and obj.name != 'Super Admin' and obj.id != member.role.id:
                return True
        return False

class CanDeleteUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            member = Member.objects.filter(user=request.user).first()
            if member and obj and obj.role.name != 'Super Admin':
                return True
        return False

class CanCreateEditTechnician(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST' or request.method == 'PUT':
            if request.user.is_authenticated:
                member = Member.objects.filter(user=request.user).first()
                if member and member.role.name == 'Operator':
                    return True
            return False
        return True  # allow GET requests

class CanSeeOwnProfileOrTechnician(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            member = Member.objects.filter(user=request.user).first()
            if member and obj:
                if obj.id == member.id or (member.role.name == 'Technician' and obj.role.name == 'Technician'):
                    return True
        return False
