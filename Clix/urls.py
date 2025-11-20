from django.urls import path, include
from django.contrib import admin

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include("shortener.urls")),
]

handler404, handler500 = 'Clix.errors.error404', 'Clix.errors.error500'
