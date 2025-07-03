from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views.student_view import StudentViewSet
from core.views.subject_view import SubjectViewSet
from core.views.classroom_view import ClassroomViewSet
from core.views.grade_view import GradeViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'classrooms', ClassroomViewSet)
router.register(r'grades', GradeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
