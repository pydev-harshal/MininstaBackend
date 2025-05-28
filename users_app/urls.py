from django.urls import path
from users_app import views

urlpatterns = [
    path('create/', views.UserProfileCreateView.as_view(), name='user-create'),
    path('detail/<str:username>/', views.UserProfileDetailView.as_view(), name='user-detail'),
    path('update/', views.UserProfileUpdateView.as_view(), name='user-update'),
    path('delete/', views.UserProfileDeleteView.as_view(), name='user-delete'),


    path('followers/<str:username>/', views.UserFollowersListView.as_view(), name='user-followers-list'),
    path('following/<str:username>/', views.UserFollowingListView.as_view(), name='user-following-list'),
]