from core.models.classrooms_model import Classrom
from core.serializers.classroom_serializer import ClassroomSerializer
from rest_framework import viewsets

class ClassroomViewSet(viewsets.ModelViewSet):
    serializer_class = ClassroomSerializer
    queryset = Classrom.objects.all()