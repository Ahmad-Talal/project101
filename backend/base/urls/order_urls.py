from django.urls import path
from base.views import order_views as views

urlpatterns=[
    path('add/', views.addOrderItems,name='orders-add'),
    path('all/', views.getAllOrders,name='my-orders'),
    path('getall/', views.getAllSellingOrders,name='my-orders'),   
    path('<str:pk>/',views.getOrdersThroughID,name='user-order'),  
    path('<str:pk>/pay/',views.updateOrderToPaid,name='pay'), 
    path('<str:pk>/ship/',views.updateOrderToShipped,name='ship'),  
]