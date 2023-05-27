from rest_framework import serializers
from Таблица_посещаемости.models import FirstTable


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FirstTable
        fields = ("esp", "group", "username", "time")