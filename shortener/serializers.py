#from rest_framework import serializers
from .models import *

#class RecipeSerializer(serializers.ModelSerializer):
  #author = serializers.ReadOnlyField(source="author.username")
  #class Meta:
    #model = Recipe
    #fields = ["id", "title", "description", "ingredients", "instructions","author", "created_at", "updated_at"]

#class CreateReportSerializer(serializers.Serializer):
    #title = serializers.CharField(required=False, allow_blank=True, max_length=200)
    #include_recipes = serializers.BooleanField(default=False)
