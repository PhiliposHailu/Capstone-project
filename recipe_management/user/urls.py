from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.UserRegisteration.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile')
]
