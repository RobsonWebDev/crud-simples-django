from django.urls import path
from .views import index, editar_pessoa, excluir_pessoa, cadastrar

app_name = 'app'

urlpatterns = [
    path('index/', index, name='index'),
    path('cadastrar/', cadastrar, name='cadastrar'),
    path('editar/<str:id>/', editar_pessoa, name='editar_pessoa'),
    path('excluir/<str:id>/', excluir_pessoa, name= 'excluir_pessoa')
]

