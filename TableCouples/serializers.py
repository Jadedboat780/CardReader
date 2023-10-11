from rest_framework import serializers
from TableCouples.models import CoupleInfo


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CoupleInfo
        fields = ("esp", "username", "id_card")
