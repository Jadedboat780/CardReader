from rest_framework import viewsets, routers, permissions
from django.urls import path, include
from Registration.models import Registration
from TableCouples.models import CoupleInfo
from Registration.serializers import TeacherSerializer
from TableCouples.serializers import StudentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = CoupleInfo.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]


router = routers.DefaultRouter()
router.register(r'teacher', TeacherViewSet)
router.register(r'couple', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
