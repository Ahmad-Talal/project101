from django.urls import path
from base.views import rescue_views as views

urlpatterns=[

    path('rescue-teams/',views.getRescueTeams,name='rescue-teams'), 
    path('create/',views.createRescue,name='createRescue'),
    path('pic/',views.uploadImage,name='image'),
]


