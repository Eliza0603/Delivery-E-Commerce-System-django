from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('admin-dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('produto/<int:pk>/', views.detalhe_produto_view, name='detalhe_produto'),
]