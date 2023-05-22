from django import forms


class FilterForm(forms.Form):
    esp = forms.CharField(label='Номер кабинета', min_length=3, max_length=3, required=False)
    group = forms.CharField(label='Номер группы', min_length=4, max_length=16, required=False)
    name = forms.CharField(label='ФИО', min_length=8, required=False)
    # time = forms.DateTimeField(label='Время прибытия', input_formats=['%d.%m %H'], required=False)


class CreateFrom(forms.Form):
    esp = forms.CharField(label='Номер кабинета', min_length=3, max_length=3)
    name = forms.CharField(label='ФИО', min_length=15)
    time = forms.DateTimeField(input_formats=['%d.%m %H:%M'])
