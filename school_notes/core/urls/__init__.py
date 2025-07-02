from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views.student_view import StudentViewSet
from core.views.subject_view import SubjectViewSet
from core.views.classrrom_view import ClassroomViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'classrooms', ClassroomViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
