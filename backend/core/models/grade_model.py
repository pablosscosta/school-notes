from django.db import models
from core.models.student_model import Student
from core.models.subject_model import Subject

class Grade(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE)
    score=models.FloatField()

    def __str__(self):
        return (
            f"A nota do aluno {self.student.first_name} {self.student.last_name} em {self.subject.name} é: {self.score}"
        )