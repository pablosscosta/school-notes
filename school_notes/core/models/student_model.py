from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=25)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"