"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin-ape/', admin.site.urls),
    #path('api/',include('base.urls')),
    path('api/products/',include('base.urls.product_urls')),
    path('api/users/',include('base.urls.user_urls')),
    path('api/orders/',include('base.urls.order_urls')),  
    path('api/stripe/',include('base.urls.stripe_urls')),  
    path('api/seller/',include('base.urls.seller_urls')),
    path('api/rescue/',include('base.urls.rescue_urls')),  
    path('api/report/',include('base.urls.report_urls')),  
    path('api/vet/',include('base.urls.vet_urls')),
    path('api/service/',include('base.urls.service_urls')),  
    path('api/appointment/',include('base.urls.appointment_urls')),
    path('api/booking/',include('base.urls.booking_urls')),  
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)