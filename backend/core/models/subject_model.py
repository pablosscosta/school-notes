from django.db import models

class Subject(models.Model):
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=100)
    workload=models.IntegerField()

    def __str__(self):
        return f"{self.name}"
