from django.urls import path
from base.views import booking_views as views

urlpatterns=[   
    # path('pending/',views.pendingAppointments,name='get_sppointment'),
    path('available-slots/<str:pk>/',views.sendSlots,name='get-slots'),  
    # path('update/<str:pk>/',views.statusAppointment,name='status_sppointment'),  
]


