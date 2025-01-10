from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterationView.as_view(), name='user_registeration'),
    path('create/', views.CreateView.as_view(), name='create_recipe'),
    path('list/', views.ListView.as_view(), name='list_recipe'),
    path('list/<int:pk>/', views.DetailView.as_view(), name='recipe_detail'),
    path('update/<int:pk>/', views.UpdateView.as_view(), name='update_recipe'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete_recipe'),
    path('filter/<int:pk>/', views.FilterView.as_view(), name='user_registeration')
]
