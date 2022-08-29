from django.urls import path
from flia.views import listar_familiares


urlpatterns = [
    path('', listar_familiares),
]