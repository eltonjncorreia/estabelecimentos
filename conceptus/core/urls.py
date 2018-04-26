from django.urls import path
from .views import dashboard, create

app_name = 'core'
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('cadastro/', create, name='create'),
]
