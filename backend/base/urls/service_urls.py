from django.urls import path
from base.views import service_views as views

urlpatterns=[

    path('',views.getServiceProviders,name='service_providers'), 
    path('create/',views.createServiceProvider,name='createServiceProvider'),
    path('pic/',views.uploadImage,name='image'),
]


