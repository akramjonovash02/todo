
from django.contrib import admin
from django.urls import path
from mainApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TasksView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add/', AddView.as_view(), name='add_task'),
    path('edit/<int:task_id>/', EditView.as_view(), name='edit_task')
]
