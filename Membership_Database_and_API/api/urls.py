from django.urls import path
from . import views

urlpatterns = [
    # AUTHENTICATION ENDPOINTS
    path('register/', views.RegisterAPI.as_view(), name='register'),
    path('login/', views.LoginAPI.as_view(), name='login'),

    # DIRECTORS ENDPOINTS
    path('directors/', views.DirectorsAPIView.as_view(), name='directors'),
    path('director/<int:pk>/', views.DirectorAPIView.as_view(), name='director'),

    # INDIVIDUAL MEMBERS ENDPOINTS
    path('individual_member/register/', views.IndividualMemberCreateAPIView.as_view(), name='individual_member_register'),
    path('individual_members/', views.IndividualMembersAPIView.as_view(), name='individual_members'),
    path('individual_member/<int:pk>/', views.IndividualMemberAPIView.as_view(), name='individual_member'),
    path('individual_member/<int:pk>/update/', views.IndividualMemberUpdateAPIView.as_view(), name='individual_member_update'),
    path('individual_member/<int:pk>/delete/', views.IndividualMemberDestroyAPIView.as_view(), name='individual_member_delete'),

    # CORPORATE MEMBERS ENDPOINTS
    path('corporate_member/register/', views.CorporateMemberCreateAPIView.as_view(), name='corporate_member_register'),
    path('corporate_members/', views.CorporateMembersAPIView.as_view(), name='corporate_members'),
    path('corporate_member/<int:pk>/', views.CorporateMemberAPIView.as_view(), name='corporate_member'),
    path('corporate_member/<int:pk>/update/', views.CorporateMemberUpdateAPIView.as_view(), name='corporate_member_update'),
    path('corporate_member/<int:pk>/delete/', views.CorporateMemberDestroyAPIView.as_view(), name='corporate_member_delete'), 
]