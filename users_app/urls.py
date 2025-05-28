from django.urls import path
from users_app import views

urlpatterns = [
    path('create/', views.UserProfileCreateView.as_view(), name='user-create')
]