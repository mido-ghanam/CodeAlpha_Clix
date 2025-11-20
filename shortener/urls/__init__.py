from django.urls import path, include
from . import *

urlpatterns = [
  path('api/', include("shortener.urls.api")),
  path('', include("shortener.urls.web")),
  #path('', include("shortern.urls")),
]
