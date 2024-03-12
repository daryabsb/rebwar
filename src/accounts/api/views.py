from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from src.accounts.models import Patient
from .serializers import PatientSerializer

@api_view(['POST'])
def create_patient(request):
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
