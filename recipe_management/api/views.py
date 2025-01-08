from rest_framework import viewsets
from django.contrib.auth import get_user_model
from recipe.models import Recipe, Category, Ingredient
from .serializers import UserSerializers, RecipeSerializers, CategorySerializers, IngredientSerializers
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

#CRUD operations view for user
class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated]

    # permission_required = [isadmin]

#CRUD operations view for recipe
class RecipeViewset(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(publisher=self.request.user)
