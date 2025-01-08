from django.urls import path, include
from .views import UserViewset, RecipeViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', UserViewset)
router.register('recipe', RecipeViewset)

urlpatterns = [] + router.urls