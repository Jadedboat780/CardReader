from rest_framework import serializers
from Таблица_посещаемости.models import FirstTable
from Регистрация.models import DjandoRegistration


class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DjandoRegistration
        fields = '__all__'


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FirstTable
        fields = '__all__'