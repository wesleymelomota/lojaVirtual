from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='core'

urlpatterns = [
    path('', views.index, name='index'), 
    path('produtos/', views.listar_produtos, name='listar_produtos'),
    path('produtos/<str:slug_categoria>/', views.listar_produtos, name='listar_produtos_por_categoria' ),
    path('produto/<str:slug_produto>/<int:id>/', views.detalhes_produtos, name='detalhes_produto')
]
