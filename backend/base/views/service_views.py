from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response


from base.models import Service
#from base.products import products
from base.serializers import ServiceProviderSerializer 

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getServiceProviders(request):
        service_providers=Service.objects.all()
        serializer= ServiceProviderSerializer(service_providers,many=True)
        return Response(serializer.data)    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createServiceProvider(request):
        user = request.user
        data = request.data
        serviceProvider=Service.objects.create(
                User=user,
                name = user.username,
                title=data['title'],
                fee=data['fee'],
                experience=data['experience'],
                services=data['qualification'],
        )
        serializer= ServiceProviderSerializer(serviceProvider,many=False)
        return Response(serializer.data)    

@api_view(['POST'])
def uploadImage(request):
        data = request.data
        service_provider_id= data['service_provider_id']
        serviceProvider=Service.objects.get(_id=service_provider_id)
        
        serviceProvider.image= request.FILES.get('image')
        serviceProvider.save()
        return Response("image was uploaded")    
