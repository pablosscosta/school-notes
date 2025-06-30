from rest_framework import routers
from core.views.student_view import StudentViewSet

router = routers.SimpleRouter()
router.register(r'students', StudentViewSet)

urlpatterns = router.urls
