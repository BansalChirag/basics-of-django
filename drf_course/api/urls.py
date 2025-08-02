from django.urls import path
from .import views

# urlpatterns = [
#     url(r'^products/$', views.ProductListView.as_view(), name='product-list'),
    
# ]

urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>/', views.product_detail),
    path('orders/', views.order_list),
]
