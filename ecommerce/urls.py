from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as view_accounts
from core import views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('catalogo/', include('catalog.urls')),
    path('contato/', views.contato, name='contato'),
    path('conta/', include('accounts.urls'), name='conta'),
    path('login/', view_accounts.LoginView.as_view(), name='login'),
    path('logout/', view_accounts.LogoutView.as_view(), name='logout'),
]
