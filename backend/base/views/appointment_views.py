from django.shortcuts import render
from datetime import date
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response


from base.models import Vet,Appointment,Booking
from base.serializers import AppointmentSerializer 
from rest_framework import status

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createAppointment(request,pk):
        try:
            data = request.data
            User = request.user
            v=Vet.objects.get(_id=pk)
            Appointment.objects.create(
            phonenumber = data['phonenumber'],
            date = date.today(),
            slot = data['slot'],
            details = data['details'],
            user = User,
            vet = v,
            )
            
            bookings=Booking.objects.filter(vet=v)
            for b in bookings:
                for k,v in b.availableSlots.items():
                    if v==data['slot']:
                        del b.availableSlots[k]
                        b.save()
            
            return Response({'detail':'appointment is Booked successfully!'})    
        except:
            return Response({'detail':'appointment is not Booked'},
                status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def pendingAppointments(request):
        user = request.user
        v= Vet.objects.get(User=user)
        try:
            appointments = Appointment.objects.filter(vet=v)
            serializer= AppointmentSerializer(appointments,many=True)
            return Response(serializer.data)    
        except:
            return Response({'detail':'appointment was not Sent'},
                status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def statusAppointment(request,pk):

        try:
            data = request.data
            appointment = Appointment.objects.get(_id=pk)
            appointment.status = data['status']
            appointment.delete()
            # for i in appointments:
            #     print(i.name)
            serializer= AppointmentSerializer(appointment,many=False)
            #appointments = Appointment.objects.all()

            return Response(serializer.data)    
        except:
            return Response({'detail':'appointment was deleted'},
                status=status.HTTP_400_BAD_REQUEST)