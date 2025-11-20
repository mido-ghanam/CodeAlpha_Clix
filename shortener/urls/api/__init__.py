from django.urls import path, include
from shortener.views import api as vAPI

urlpatterns = [
  path('short/create/', vAPI.ShortURL.ShortURLCreate.as_view(), name="shortLinkCreateAPI"),
  #path('', include("shortener.urls.web")),
  #path('', include("shortern.urls")),
]
