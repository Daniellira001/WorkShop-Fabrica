from django.contrib import admin
from django.urls import path, include
from carro.views import UsuarioViewSet, CarroUsoViwSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Usuario', UsuarioViewSet)
router.register(r'CarroUso', CarroUsoViwSet)

urlpatterns = [
    path('CarroUso/', include(router.urls)),
    path('Usuario/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
