from django.urls import path, include
from app_cad_usuarios import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    # rota, view responsável, nome de referência
    # credenciamento.com
    path('',views.home,name='home'),
    # credenciamento.com/usuarios
    path('usuarios/', views.usuarios,name='listagem_usuarios'),
    # Login
    path('auth/', include('app_login.urls'))
]
