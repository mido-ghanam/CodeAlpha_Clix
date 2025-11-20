from shortener.views import web
from django.urls import path
from . import *

urlpatterns = [
  path('', web.index, name="index"),
  path('<str:short_code>', web.routing, name="routing"),

]
