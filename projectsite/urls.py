from django.contrib import admin
from django.urls import path

from studentorg.views import HomePageView, OrganizationList, OrganizationCreateView,OrganizationUpdateView, OrganizationDeleteView
from studentorg import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('organization_list', OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/<pk>', OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/<pk>/delete', OrganizationDeleteView.as_view(), name='organization-delete'),


 # OrgMember
    path('orgmember/', views.OrgMemberListView.as_view(), name='orgmember-list'),
    path('orgmember/add/', views.OrgMemberCreateView.as_view(), name='orgmember-add'),
    path('orgmember/<int:pk>/edit/', views.OrgMemberUpdateView.as_view(), name='orgmember-edit'),
    path('orgmember/<int:pk>/delete/', views.OrgMemberDeleteView.as_view(), name='orgmember-delete'),

    # Student
    path('student/', views.StudentListView.as_view(), name='student-list'),
    path('student/add/', views.StudentCreateView.as_view(), name='student-add'),
    path('student/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student-edit'),
    path('student/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student-delete'),

    # College
    path('college/', views.CollegeListView.as_view(), name='college-list'),
    path('college/add/', views.CollegeCreateView.as_view(), name='college-add'),
    path('college/<int:pk>/edit/', views.CollegeUpdateView.as_view(), name='college-edit'),
    path('college/<int:pk>/delete/', views.CollegeDeleteView.as_view(), name='college-delete'),

    # Program
    path('program/', views.ProgramListView.as_view(), name='program-list'),
    path('program/add/', views.ProgramCreateView.as_view(), name='program-add'),
    path('program/<int:pk>/edit/', views.ProgramUpdateView.as_view(), name='program-edit'),
    path('program/<int:pk>/delete/', views.ProgramDeleteView.as_view(), name='program-delete'),
]