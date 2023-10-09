from rest_framework import serializers
from TableCouples.models import CoupleInfo


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CoupleInfo
        fields = ("username", "id_card")
