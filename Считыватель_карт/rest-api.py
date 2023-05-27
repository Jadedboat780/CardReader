from rest_framework import viewsets, routers, permissions
from django.urls import path, include
from Регистрация.models import DjandoRegistration
from Таблица_посещаемости.models import FirstTable
from Регистрация.serializers import TeacherSerializer
from Таблица_посещаемости.serializers import StudentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = DjandoRegistration.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = FirstTable.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]


router = routers.DefaultRouter()
router.register(r'teacher', TeacherViewSet)
router.register(r'couple', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
