from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('category/create/', views.AddCategoryView.as_view(), name='add-category'),
    path('category/', views.CategoryListView.as_view(), name='category-list'),
    path('category/edit/<int:pk>/', views.CategoryEditView.as_view(), name='edit-category'),
    path('category/delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='delete-category'),
    path('product/', views.ProductListView.as_view(), name='product-list'),
    path('product/create/', views.AddProductView.as_view(), name='add-product'),
    path('product/edit/<int:pk>/', views.ProductEditView.as_view(), name='edit-product'),
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete-product'),
    path('order/create/', views.CreateOrderView.as_view(), name='add-order'),
    path('order/', views.OrderListView.as_view(), name='order-list'),
    path('order/edit/<int:pk>/', views.OrderEditView.as_view(), name='edit-order'),
    path('order/delete/<int:pk>/', views.OrderDeleteView.as_view(), name='delete-order'),
    path('order/details/<int:pk>/', views.OrderDetailView.as_view(), name='order-details'),
]