from rest_framework import serializers
from core.models.classrooms_model import Classrom

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classrom
        fields = "__all__"