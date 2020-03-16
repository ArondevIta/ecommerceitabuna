from django.contrib import admin
from django.urls import path, include
from core import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contato, name='contato'),
    path('catalogo/', include('catalog.urls')),
    path('admin/', admin.site.urls),
]
