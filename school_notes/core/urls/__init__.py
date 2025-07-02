from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views.student_view import StudentViewSet
from core.views.subject_view import SubjectViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'subjects', SubjectViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
