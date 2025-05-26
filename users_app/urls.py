from django.urls import path
from users_app import views

urlpatterns = [
    path('create/', views.UserCreateView.as_view(), name='user-create')
]