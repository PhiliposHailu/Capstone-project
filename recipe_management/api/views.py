from rest_framework import viewsets
from django.contrib.auth import get_user_model
from recipe.models import Recipe, Category
from .serializers import UserSerializers, RecipeSerializers, CategorySerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

User = get_user_model()

#CRUD opetation api views
class CreateView(generics.CreateAPIView):

    serializer_class = RecipeSerializers

class ListView(generics.ListAPIView):

    serializer_class = RecipeSerializers
    queryset = Recipe.objects.all()

class UpdateView(generics.ListAPIView):

    serializer_class = RecipeSerializers
    queryset = Recipe.objects.all()

class DeleteView(generics.DestroyAPIView):

    serializer_class = RecipeSerializers
    queryset = Recipe.objects.all()

class DetailView(generics.RetrieveAPIView):

    serializer_class = RecipeSerializers
    queryset = Recipe.objects.all()

#new user registeration apiview

class RegisterationView(generics.CreateAPIView):

    serializer_class = UserSerializers





# #CRUD operations view for user
# class UserViewset(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializers
#     permission_classes = [IsAuthenticated]

#     # permission_required = [isadmin]

# #CRUD operations view for recipe
# class RecipeViewset(viewsets.ModelViewSet):
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializers
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(publisher=self.request.user)
