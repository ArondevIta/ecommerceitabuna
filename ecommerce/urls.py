from django.contrib import admin
from django.urls import path
from core import views
urlpatterns = [
    path('', views.index, name='index'),
    path('contato', views.contato, name='contato'),
    path('produto', views.product, name='produto'),
    path('produtos', views.product_list, name='produtos'),
    path('admin/', admin.site.urls),
]
