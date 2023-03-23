from django.urls import path
from . import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('perfil/', views.perfil, name='perfil'),
    path('', TemplateView.as_view(template_name='index.html')),
    path('js/vue.js', TemplateView.as_view(template_name='vue.js')),
    path('js/main.js', TemplateView.as_view(template_name='main.js')),
]
