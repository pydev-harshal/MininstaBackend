from django.urls import path
from users_app import views

urlpatterns = [
    path('create/', views.UserCreateView.as_view(), name='user-create'),
    path('profile/', views.UserProfileView.as_view(), name='user-profile'),
    path('update/', views.UserUpdateView.as_view(), name='user-update'),
    path('delete/', views.UserDeleteView.as_view(), name='user-delete'),
    path('@<str:username>/', views.UserDetailsView.as_view(), name='user-details'),
]