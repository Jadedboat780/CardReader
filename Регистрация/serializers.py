from rest_framework import serializers
from Регистрация.models import DjandoRegistration


class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DjandoRegistration
        fields = ("login", "password")

