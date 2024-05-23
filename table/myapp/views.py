from rest_framework import viewsets
from .models import JobData
from .serializer import JobDataSerializer

class JobDataViewSet(viewsets.ModelViewSet):
    queryset = JobData.objects.all()
    serializer_class = JobDataSerializer
