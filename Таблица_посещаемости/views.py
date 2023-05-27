from rest_framework.response import Response
from rest_framework.views import APIView
from Таблица_посещаемости.models import FirstTable
from django.db.models import Q
from Таблица_посещаемости.serializers import StudentSerializer
from datetime import datetime


class DataBase:
    def create(self, data):
        try:
            esp = data.cleaned_data['esp']
            name = data.cleaned_data['name']
            time = data.cleaned_data['time']
            time = time.replace(year=datetime.now().year)
            FirstTable.objects.create(esp=esp, username=name, time=f"{time}").save()
        except:
            pass

    def delete(self):
        pass


class TableApiView(APIView):
    def get(self, request):
        queryset = FirstTable.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

