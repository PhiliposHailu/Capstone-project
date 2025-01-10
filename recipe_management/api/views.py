from django.contrib.auth import get_user_model
from recipe.models import Recipe
from .serializers import UserSerializers, RecipeSerializers
from rest_framework.permissions import AllowAny, IsAuthenticated, SAFE_METHODS, BasePermission
from rest_framework import generics

User = get_user_model()

# Custom Pemission Class
class RecipUserEditPermission(BasePermission):

    message = "Editing recipe is restricted to the publisher only."
    
    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
        
        return obj.publisher == request.user

#CRUD opetation Api Views

    #create new recipe
class CreateView(generics.ListCreateAPIView):

    queryset = Recipe.objects.all()
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

#New User API Registeration View
class RegisterationView(generics.CreateAPIView):

    serializer_class = UserSerializers
    #apply a view level permission that overrides our project level 
    #permission in order to allow anyone to register(create an account)
    permission_classes = [AllowAny]


# FilterView

class FilterView(generics.ListAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = RecipeSerializers

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Recipe.objects.filter(publisher=pk)
