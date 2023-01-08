from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_veiculos, name='index'),
    path('listar', views.listar_veiculos, name='listar_veiculos'),
    path('cadastrar/', views.cadastrar_veiculo, name='cadastrar_veiculos'),
    path('editar/<int:id>', views.editar_veiculo, name='editar_veiculo'),
    path('deletar/<int:id>', views.deletar_veiculo, name='deletar_veiculo'),
    path('listar/export_pdf', views.export_pdf, name='export_pdf'),
    path('listar/export_csv', views.export_csv, name='export_csv'),
]
