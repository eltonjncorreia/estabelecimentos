from django.urls import path
from .views import dashboard, create, editar

app_name = 'core'
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('cadastro/', create, name='create'),
    path('editar/<slug:slug>/', editar, name='editar'),
]
