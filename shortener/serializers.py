from rest_framework import serializers
from .models import *

class ShortURLCreate(serializers.Serializer):
  url = serializers.URLField()
  
  
#class CreateReportSerializer():
    #title = serializers.CharField(required=False, allow_blank=True, max_length=200)
    #include_recipes = serializers.BooleanField(default=False)
