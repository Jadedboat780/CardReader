from django.shortcuts import render
from rest_framework.views import APIView
from TableCouples.models import CoupleInfo
from django.db.models import Q
from datetime import datetime


class DataBase:
    def create(self, data):
        try:
            esp = data.cleaned_data['esp']
            name = data.cleaned_data['name']
            time = data.cleaned_data['time']
            time = time.replace(year=datetime.now().year)
            CoupleInfo.objects.create(esp=esp, username=name, time=f"{time}").save()
        except:
            pass

    def serach(self, queryset):
        result = CoupleInfo.objects.filter(Q(username=queryset['username']) | Q(group=queryset['group'])
                                           | Q(time=queryset['time']))
        return result

    def delete(self):
        pass



class Table(APIView):
    def get(self, request):
        qeryset = CoupleInfo.objects.all().values()
        return render(request, 'table.html', {'database': qeryset})