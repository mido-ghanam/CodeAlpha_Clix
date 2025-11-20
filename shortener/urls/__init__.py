from django.urls import path, include
from django.http import HttpResponse
from . import *

def favicon(request): return HttpResponse(status=204)

urlpatterns = [
  path('favicon.ico', favicon),
  path('api/', include("shortener.urls.api")),
  path('', include("shortener.urls.web")),
]
