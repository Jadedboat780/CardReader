from django.shortcuts import render
from Таблица_посещаемости.models import FirstTable
from rest_framework.response import Response
from rest_framework import routers, serializers, viewsets


# class TableSerializer(serializers.Serializer):
#     esp = serializers.CharField()
#     group = serializers.CharField()
#     username = serializers.CharField()
#
#
# class Rest_API:
#     def get(self, request):
#         model = FirstTable.objects.all()
#         serializer = TableSerializer(model, many=True)
#         return Response({'serializer': serializer.data})


def error_404(request, exception):
    return render(request, '404.html', status=404)