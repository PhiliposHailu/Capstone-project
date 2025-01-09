from rest_framework import viewsets
from django.contrib.auth import get_user_model
from recipe.models import Recipe, Category
from .serializers import UserSerializers, RecipeSerializers, CategorySerializers
from rest_framework.permissions import AllowAny, IsAuthenticated, SAFE_METHODS, BasePermission
from rest_framework import generics

User = get_user_model()

#custom permission that allows only the publisher
#of the recipe to delete or update it
class RecipUserEditPermission(BasePermission):

    message = "Editing recipe is restricted to the publisher only."
    
    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
        
        return obj.publisher == request.user

#CRUD opetation api views

    #create new recipe
class CreateView(generics.CreateAPIView):

    serializer_class = RecipeSerializers

    #list recipes
class ListView(generics.ListAPIView):

    serializer_class = RecipeSerializers
    queryset = Recipe.objects.all()

    #update a recipe
class UpdateView(generics.RetrieveUpdateAPIView):

    serializer_class = RecipeSerializers
    queryset = Recipe.objects.all()
        #only the publisher can update their recipe
    permission_classes = [RecipUserEditPermission]

    #delete a recipe
class DeleteView(generics.RetrieveDestroyAPIView):
    
    serializer_class = RecipeSerializers
    queryset = Recipe.objects.all()
        #only the publisher can delete their recipe
    permission_classes = [RecipUserEditPermission]

class DetailView(generics.RetrieveAPIView):

    serializer_class = RecipeSerializers
    queryset = Recipe.objects.all()

#new user registeration apiview
class RegisterationView(generics.CreateAPIView):

    serializer_class = UserSerializers
    #apply a view level that override our project level 
    #permission in order to allow anyone to register(create an account)
    permission_classes = [AllowAny]





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
