from django.contrib import admin
from django.urls import path, include  # <- añadimos include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('actividad05.urls')),  # <- conectamos nuestra app
]
