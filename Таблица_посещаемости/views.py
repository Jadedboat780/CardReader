from django.shortcuts import render
from Таблица_посещаемости.models import FirstTable
from Таблица_посещаемости.form import FilterForm


def context(room_number, group_number, time):
    if room_number and group_number and time:
        attendance_table = FirstTable.objects.filter(esp=room_number, group=group_number,
                                                     time__month=time.strftime('%m'),
                                                     time__day=time.strftime('%d'),
                                                     time__hour=time.strftime('%H')).values()
    elif room_number and group_number:
        attendance_table = FirstTable.objects.filter(esp=room_number, group=group_number).values()
    elif room_number and time:
        attendance_table = FirstTable.objects.filter(esp=room_number,
                                                     time__month=time.strftime('%m'),
                                                     time__day=time.strftime('%d'),
                                                     time__hour=time.strftime('%H')).values()
    elif group_number and time:
        attendance_table = FirstTable.objects.filter(group=group_number,
                                                     time__month=time.strftime('%m'),
                                                     time__day=time.strftime('%d'),
                                                     time__hour=time.strftime('%H')).values()
    elif room_number:
        attendance_table = FirstTable.objects.filter(esp=room_number).values()
    elif group_number:
        attendance_table = FirstTable.objects.filter(group=group_number).values()
    elif time:
        attendance_table = FirstTable.objects.filter(time__month=time.strftime('%m'),
                                                     time__day=time.strftime('%d'),
                                                     time__hour=time.strftime('%H')).values()
    else:
        attendance_table = FirstTable.objects.all().values()

    return attendance_table


def table(request):
    form = FilterForm
    if request.method == 'GET':
        attendance_table = FirstTable.objects.all().values()
        return render(request, 'table_attendance.html', {'attendance_table': attendance_table, 'form': form})

    if request.method == 'POST':
        data = request.POST
        filter_form = FilterForm(data)
        if filter_form.is_valid():
            room_number = filter_form.cleaned_data['esp']
            group_number = filter_form.cleaned_data['group']
            time = filter_form.cleaned_data['time']
            attendance_table = context(room_number, group_number, time)
        else:
            attendance_table = FirstTable.objects.all().values()
        return render(request, 'table_attendance.html', {'attendance_table': attendance_table, 'form': form})
