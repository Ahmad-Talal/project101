from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response


from base.models import Report,Rescue
from base.serializers import ReportSerializer 
from rest_framework import status

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createReport(request,pk):
        try:
            data = request.data
            user = request.user
            r=Rescue.objects.get(_id=pk)
            report = Report.objects.create(
                user = user,
                rescue = r,
                phonenumber = data['phonenumber'],
                location = data['location'],
                assign = pk,
                details = data['details']
            )
            serializer= ReportSerializer(report,many=False)
            return Response({'detail':'Report Sent successfully!! Great Job'})    
        except:
            return Response({'detail':'Report was not Sent'},
                status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def getReports(request):
    user = request.user
    reports = Report.objects.all()
    sendReports =[]
    for report in reports:
        if report.rescue.User == user:
            sendReports.append(report) 
    serializer= ReportSerializer(sendReports,many=True)
    return Response(serializer.data)