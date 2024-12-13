

from django.contrib import admin
from django.urls import path, include,get_resolver
from . import views

app_name= "app_alumnalia"

urlpatterns = [
    path("", views.InicioView.as_view(), name= 'inicio'),
    path("inicio/", views.InicioView.as_view(), name= 'inicio'),
#    path('__debug__/', include('debug_toolbar.urls')),
    path("datos_personales/", views.datos_personales_view.as_view(), name= 'datos_personales'),
    path('datos_formador/', views.datos_formador_view.as_view(), name='datos_formador')
]
print(f" control --> {get_resolver().reverse_dict.keys()} <")
