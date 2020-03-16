from django.urls import path
from catalog import views


urlpatterns = [
    path('', views.product_list, name='produtos'),
    path('<slug:slug>', views.category, name='categoria'),
    path('produtos/<slug:slug>/', views.product, name='produto')
]
