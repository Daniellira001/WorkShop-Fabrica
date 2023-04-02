from django.contrib import admin
from django.urls import path, include
from carro.views import UsuarioViewSet, CarroUsoViwSet, CarroUsodelete, Usuariodelete




urlpatterns = [
    path('CarroUso/', CarroUsoViwSet.as_view()),
    path('Usuario/', UsuarioViewSet.as_view()),
    path('admin/', admin.site.urls),
    path('CarroUso/<int:pk>/', CarroUsodelete.as_view()),
    path('Usuario/<int:pk>/', Usuariodelete.as_view()),
    path('api-auth/', include('rest_framework.urls'))
]
