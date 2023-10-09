from rest_framework import serializers
from Registration.models import Registration


class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registration
        fields = ("username", "login", "password")

