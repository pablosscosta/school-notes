from rest_framework import viewsets
from core.serializers.subject_serializer import SubjectSerializer
from core.models.subject_model import Subject

class SubjectViewSet(viewsets.ModelViewSet):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()