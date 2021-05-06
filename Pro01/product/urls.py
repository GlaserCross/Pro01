from django.urls import path 
from . import views

urlpatterns = [
	path('<str:pk>',views.ProductDetailView.as_view(),name='product_detail'),
	path('create/',views.ProductCreate.as_view(),name='product_create'),
	path('<str:pk>/update/',views.ProductUpdate.as_view(),name='product_update'),	
	path('<str:pk>/delete/',views.ProductDelete.as_view(),name='product_delete'),
	path('productos/',views.productos,name='productos'),
]