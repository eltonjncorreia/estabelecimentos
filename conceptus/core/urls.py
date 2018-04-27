from django.urls import path
from .views import dashboard, create, editar, deletar

app_name = 'core'
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('cadastro/', create, name='create'),
    path('editar/<int:pk>/', editar, name='editar'),
    path('deletar/<slug:slug>/', deletar, name='deletar'),
]
