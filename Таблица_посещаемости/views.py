from django.shortcuts import render
from django.http import JsonResponse
from Таблица_посещаемости.models import FirstTable
from Таблица_посещаемости.form import CreateFrom, FilterForm
from django.db.models import Q

# def context(room_number, group_number, time):
#     if room_number and group_number and time:
#         attendance_table = FirstTable.objects.filter(esp=room_number, group=group_number,
#                                                      time__month=time.strftime('%m'),
#                                                      time__day=time.strftime('%d'),
#                                                      time__hour=time.strftime('%H')).values()
#     elif room_number and group_number:
#         attendance_table = FirstTable.objects.filter(esp=room_number, group=group_number).values()
#     elif room_number and time:
#         attendance_table = FirstTable.objects.filter(esp=room_number,
#                                                      time__month=time.strftime('%m'),
#                                                      time__day=time.strftime('%d'),
#                                                      time__hour=time.strftime('%H')).values()
#     elif group_number and time:
#         attendance_table = FirstTable.objects.filter(group=group_number,
#                                                      time__month=time.strftime('%m'),
#                                                      time__day=time.strftime('%d'),
#                                                      time__hour=time.strftime('%H')).values()
#     elif room_number:
#         attendance_table = FirstTable.objects.filter(esp=room_number).values()
#     elif group_number:
#         attendance_table = FirstTable.objects.filter(group=group_number).values()
#     elif time:
#         attendance_table = FirstTable.objects.filter(time__month=time.strftime('%m'),
#                                                      time__day=time.strftime('%d'),
#                                                      time__hour=time.strftime('%H')).values()
#     else:
#         attendance_table = FirstTable.objects.all().values()
#
#     return attendance_table
# def create(form):
#     esp = form.cleaned_data['esp']
#     name = form.cleaned_data['name']
#     time = form.cleaned_data['time']
#     time = time.replace(year=2023)
#     FirstTable.objects.create(esp=esp, username=name, time=f"{time}").save()


def table(request):
    form_1 = FilterForm
    form_2 = CreateFrom

    if request.method == 'GET':
        attendance_table = FirstTable.objects.all().values()
        print(JsonResponse(attendance_table, safe=False))
        return render(request, 'table_attendance.html', {'attendance_table': attendance_table, 'form': [form_1, form_2]})

    if request.method == 'POST':
        data = request.POST
        # create_form = CreateFrom(data)
        filter_form = FilterForm(data)
        if filter_form.is_valid():
            room_number = filter_form.cleaned_data['esp']
            group_number = filter_form.cleaned_data['group']
            student_name = filter_form.cleaned_data['name']
            # time = filter_form.cleaned_data['time']
            attendance_table = FirstTable.objects.filter(
                Q(esp=room_number) | Q(group=group_number) | Q(username=student_name)
            ).values()
        else:
            attendance_table = FirstTable.objects.all().values()
        # if create_form.is_valid():
        #     create(create_form)
        return render(request, 'table_attendance.html', {'attendance_table': attendance_table, 'form': [form_1, form_2]})

