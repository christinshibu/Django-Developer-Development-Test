from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # login / logout
    path('login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # pages
    path('', views.dashboard, name='dashboard'),
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.product_form, name='product_add'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/<int:pk>/edit/', views.product_form, name='product_edit'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
]
