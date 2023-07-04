from django.urls import path
from .views import home,poblar_bd,Producto, RegisterView

urlpatterns = [
    # Otras URLs de la aplicación...
    path('registrar/', RegisterView.as_view(template_name='registration/register.html'), name='register'),
]

from django.urls import path, include

urlpatterns = [
    # ... otras URLs de tu proyecto ...
    path('accounts/', include('allauth.urls')),  # Para Django Allauth
    # O
    path('accounts/', include('registration.backends.default.urls')),  # Para Django Registration Redux
]

urlpatterns = [
    path('', home, name="home"),
    path('poblar_bd', poblar_bd, name="poblar_bd"),
    path('producto/<action>/<id>', Producto, name="producto"),
    #path('ver_datos_persona/', ver_datos_persona, name="ver_datos_persona"),
]
