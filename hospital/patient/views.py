from rest_framework.response import Response
from .models import Patient
from .serializers import PatientSerializer
from rest_framework.decorators import api_view




@api_view(['GET'])
def getPatient(req):
    Patients=Patient.objects.all()
    serializer=PatientSerializer(Patients,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addPatient(req):
    serializer=PatientSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getSinglePatient(req,pk):
    Patients=Patient.objects.get(id=pk)
    serializer=PatientSerializer(Patients,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updatePatient(req,pk):
    name=Patient.objects.get(id=pk)
    data=req.data
    serializer=PatientSerializer(instance=name,data=data,many=False)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deletePatient(req,pk):
    Patient.objects.get(id=pk).delete()
    return Response("Successfully Deleted")