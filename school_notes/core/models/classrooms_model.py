from django.db import models
from core.models.subject_model import Subject

class Classrom(models.Model):
    PERIODS_CHOICES = {
        "M": "Matutino",
        "V": "Vespertino",
        "N": "Noturno",
        "I": "Integral",
    }

    name=models.CharField(max_length=15)
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE)
    period=models.CharField(max_length=1, choices=PERIODS_CHOICES)
    room_number=models.IntegerField()

    def __str__(self):
        return f"{self.name}"