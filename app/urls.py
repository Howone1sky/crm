from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('settings/general/subjects/', views.settings_general_subjects, name='settings_general_subjects'),
    path('settings/general/levels/', views.settings_general_levels, name='settings_general_levels'),
    path('settings/general/ages/', views.AgeCategoryAdd.as_view(), name='settings_general_ages'),
    path('settings/members/status/', views.settings_members_status, name='settings_members_status'),
    path('settings/members/roles/', views.settings_members_roles, name='settings_members_roles'),
    path('settings/members/permissions/', views.settings_members_perms, name='settings_members_perms'),
    path('settings/members/permissions/<int:role_id>/', views.settings_members_perms, name='settings_members_perms'),
    path('company/members/', views.company_members, name='company_members'),
    path('company/members/add/', views.company_members_add, name='company_members_add'),
    path('company/members/<int:uid>/', views.member_profile, name='company_members_profile'),
    path('company/schools/', views.company_schools, name='company_schools'),
    path('company/schools/add/', views.CompanySchoolsAdd.as_view(), name='company_schools_add'),
    path('company/schools/add_room/', views.CompanySchoolsAddRoom.as_view(), name='company_schools_add_room'),
    path('company/schools/add_room/<int:sid>/', views.CompanySchoolsAddRoom.as_view(), name='company_schools_add_room'),
    path('company/camps/', views.company_camps, name='company_camps'),
    path('company/camps/', views.company_camps, name='company_camps'),
    path('company/camps/add/', views.CompanyCampsAdd.as_view(), name='company_camps_add'),
    path('learning/students/', views.learning_students, name='learning_students'),
    path('company/salaries', views.company_salaries, name='company_salaries'),
    path('company/salaries/add/', views.CompanySalaryAdd.as_view(), name='company_salaries_add'),
    path('learning/groups/', views.learning_groups, name='learning_groups'),
    path('learning/groups/add/', views.LearningGroupsAdd.as_view(), name='learning_groups_add'),
    path('learning/groups/<int:pk>/', views.LearningGroupsDetails.as_view(), name='learning_groups_details'),
    path('learning/groups/add_student/', views.LearningGroupStudentAdd.as_view(),
         name='learning_groups_add_student'),
    path('learning/groups/add_student/<int:pk>/', views.LearningGroupStudentAdd.as_view(),
         name='learning_groups_add_student'),
    path('learning/groups/add_schedule/', views.LearningGroupScheduleAdd.as_view(),
         name='learning_groups_add_schedule'),
    path('learning/groups/add_schedule/<int:pk>/', views.LearningGroupScheduleAdd.as_view(),
         name='learning_groups_add_schedule'),
]
