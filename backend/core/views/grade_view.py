from rest_framework import viewsets
from core.models.grade_model import Grade
from core.serializers.grade_serializer import GradeSerializer

class GradeViewSet(viewsets.ModelViewSet):
    serializer_class = GradeSerializer
    queryset = Grade.objects.all()