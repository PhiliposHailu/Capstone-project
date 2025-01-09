from django.urls import path
from . import views
# from .views import UserViewset, RecipeViewset
# from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('create/', views.CreateView.as_view(), name='create_recipe'),
    path('list/', views.ListView.as_view(), name='list_recipe'),
    path('list/<int:pk>/', views.DetailView.as_view(), name='recipe_detail'),
    path('update/<int:pk>/', views.UpdateView.as_view(), name='update_recipe'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete_recipe'),
]











# router = DefaultRouter()
# router.register('user', UserViewset)
# router.register('recipe', RecipeViewset)

# urlpatterns = [] + router.urls