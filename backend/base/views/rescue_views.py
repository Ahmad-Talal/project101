from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response


from base.models import Rescue
#from base.products import products
from base.serializers import RescueSerializer 

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getRescueTeams(request):
        rescues=Rescue.objects.all()
        serializer= RescueSerializer(rescues,many=True)
        return Response(serializer.data)    


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createRescue(request):
        user = request.user
        data = request.data
        print("Aaya")
        rescue=Rescue.objects.create(
                User=user,
                name = user.username,
                title=data['title'],
                background=data['background'],
                experience=data['experience'],
                rating=data['experience'],
                location = "31.344 , 33.566",
                description=data['description'],
        )
        serializer= RescueSerializer(rescue,many=False)
        return Response(serializer.data)    

@api_view(['POST'])
def uploadImage(request):
        data = request.data
        rescue_id= data['rescue_id']
        rescue=Rescue.objects.get(_id=rescue_id)
        
        rescue.image= request.FILES.get('image')
        rescue.save()
        return Response("image was uploaded")   