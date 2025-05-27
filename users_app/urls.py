from django.urls import path
from users_app import views

urlpatterns = [
    path('@<str:username>/', views.UserDetailView.as_view(), name='user-detail'),
    path('create/', views.UserCreateView.as_view(), name='user-create'),
    path('update/', views.UserUpdateView.as_view(), name='user-update'),
    path('delete/', views.UserDeleteView.as_view(), name='user-delete'),
]