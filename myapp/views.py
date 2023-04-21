from rest_framework import generics, permissions
from .models import Role, Right, Member
from .serializers import RoleSerializer, RightSerializer, MemberSerializer, MemberCreateSerializer, MemberUpdateSerializer
from .permissions import IsSuperAdminOrAdmin, IsAdmin, IsOperator, IsTechnician, CanEditRole, CanDeleteUser, CanCreateEditTechnician, CanSeeOwnProfileOrTechnician

class RoleListCreateView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsSuperAdminOrAdmin]

class RoleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsSuperAdminOrAdmin, CanEditRole]

class RightListCreateView(generics.ListCreateAPIView):
    queryset = Right.objects.all()
    serializer_class = RightSerializer
    permission_classes = [IsSuperAdminOrAdmin]

class RightDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Right.objects.all()
    serializer_class = RightSerializer
    permission_classes = [IsSuperAdminOrAdmin]

class MemberListView(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsSuperAdminOrAdmin]

class MemberCreateView(generics.CreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberCreateSerializer
    permission_classes = [IsSuperAdminOrAdmin]

class MemberDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberUpdateSerializer
    permission_classes = [IsSuperAdminOrAdmin, CanSeeOwnProfileOrTechnician, CanDeleteUser]

class TechnicianListView(generics.ListAPIView):
    queryset = Member.objects.filter(role__name='Technician')
    serializer_class = MemberSerializer
    permission_classes = [IsSuperAdminOrAdmin]

class TechnicianCreateView(generics.CreateAPIView):
    queryset = Member.objects.filter(role__name='Technician')
    serializer_class = MemberCreateSerializer
    permission_classes = [IsSuperAdminOrAdmin, CanCreateEditTechnician]

class TechnicianDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.filter(role__name='Technician')
    serializer_class = MemberUpdateSerializer
    permission_classes = [IsSuperAdminOrAdmin, CanSeeOwnProfileOrTechnician, CanDeleteUser]

class OperatorCreateView(generics.CreateAPIView):
    queryset = Member.objects.filter(role__name='Operator')
    serializer_class = MemberCreateSerializer
    permission_classes = [IsSuperAdminOrAdmin]

class OperatorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.filter(role__name='Operator')
    serializer_class = MemberUpdateSerializer
    permission_classes = [IsSuperAdminOrAdmin, CanSeeOwnProfileOrTechnician, CanDeleteUser]
