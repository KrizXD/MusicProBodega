from django.urls import path
from . import views
from .views import mostrar_productos

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('saludo/', views.mi_vista, name='saludo'),
    path('productos/', mostrar_productos, name='productos'),
]
