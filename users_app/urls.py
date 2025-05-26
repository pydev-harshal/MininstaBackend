from django.urls import path
from users_app import views

urlpatterns = [
    path('list/', views.UserListView.as_view(), name='user-list'),
    path('create/', views.UserCreateView.as_view(), name='user-create'),
    path('detail/', views.UserDetailView.as_view(), name='user-detail'),
    path('update/', views.UserUpdateView.as_view(), name='user-update'),
    path('delete/', views.UserDeleteView.as_view(), name='user-delete'),
    path('@<str:username>/', views.UserProfileView.as_view(), name='user-profile'),
]