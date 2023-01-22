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
    path('veiculo/obter_marca/<int:id>', views.obter_marca_veiculo, name='obter_marca'),
    path('veiculo/delete_all', views.delete_all, name='delete_all'),
]
