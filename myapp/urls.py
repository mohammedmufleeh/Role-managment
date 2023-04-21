from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('roles/', RoleListCreateView.as_view(), name='role-list-create'),
    path('roles/<int:pk>/', RoleDetailView.as_view(), name='role-detail'),
    path('rights/', RightListCreateView.as_view(), name='right-list-create'),
    path('rights/<int:pk>/', RightDetailView.as_view(), name='right-detail'),
    path('members/', MemberListView.as_view(), name='member-list'),
    path('members/create/', MemberCreateView.as_view(), name='member-create'),
    path('members/<int:pk>/', MemberDetailView.as_view(), name='member-detail'),
    path('technicians/', TechnicianListView.as_view(), name='technician-list'),
    path('technicians/create/', TechnicianCreateView.as_view(), name='technician-create'),
    path('technicians/<int:pk>/', TechnicianDetailView.as_view(), name='technician-detail'),
    path('operators/create/', OperatorCreateView.as_view(), name='operator-create'),
    path('operators/<int:pk>/', OperatorDetailView.as_view(), name='operator-detail'),
]
