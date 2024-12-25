from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),  # Define logout URL here
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-employee/', views.add_employee, name='add_employee'),
    path('list/', views.employee_list, name='employee_list'),
    path('add-employee/', views.add_employee, name='add_employee'),
    path('employees/', views.employee_list, name='employee_list'),
    path('edit-employee/<int:id>/', views.edit_employee, name='edit_employee'),
    path('force-logout/', views.force_logout, name='force_logout'),
    path('edit-employee/<int:id>/', views.edit_employee, name='edit_employee'),  # Edit URL
    path('delete-employee/<int:id>/', views.delete_employee, name='delete_employee'),  # Delete URL

]
