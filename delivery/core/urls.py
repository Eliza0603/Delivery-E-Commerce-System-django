from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produto/<int:pk>/', views.detalhe_produto_view, name='detalhe_produto'),
    path('login/', views.login_view, name='login'),
    path('admin-dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    
    # Novas rotas que acabamos de criar:
    path('admin/cadastrar-produto/', views.cadastrar_produto_view, name='cadastrar_produto'),
    path('acompanhar-pedido/', views.acompanhar_pedido_view, name='acompanhar_pedido'),
]