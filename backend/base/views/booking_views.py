from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from datetime import date

from base.models import Vet,Appointment,Booking
from base.serializers import BookingSerializer 
from rest_framework import status



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def sendSlots(request,pk):
        try:
            v= Vet.objects.get(_id=pk)
            bookings=Booking.objects.filter(vet=v)
            if bookings:
                for b in bookings:
                    if b.date==str(date.today()):
                        serializer= BookingSerializer(b,many=False)
                        return Response(serializer.data)
                    else:
                        b.date=str(date.today())
                        b.availableSlots= {
                        1 : "6-7",
                        2:  "7-8",
                        3:  "8-9"
                        }
                        b.vet = v
                        b.save()
                        serializer= BookingSerializer(b,many=False)
                        return Response(serializer.data) 
            else:
                booking=Booking.objects.create(
                    vet = v,
                    availableSlots = {
                        1 : "6-7",
                        2:  "7-8",
                        3:  "8-9"
                    },
                    date = date.today()
                )
                serializer= BookingSerializer(booking,many=False)
                return Response(serializer.data)  
        except:
            return Response({'detail':'booking was not Sent'},
                status=status.HTTP_400_BAD_REQUEST)
