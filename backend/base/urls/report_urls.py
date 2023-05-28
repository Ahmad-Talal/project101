from django.urls import path
from base.views import report_views as views

urlpatterns=[
    path('get/',views.getReports,name='reports'),  
    path('create/<str:pk>/',views.createReport,name='create_report'),  
]


