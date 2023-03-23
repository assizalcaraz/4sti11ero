from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('perfil/', views.perfil, name='perfil'),
]
