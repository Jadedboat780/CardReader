from django import forms


class RegisterForm(forms.Form):
    login = forms.CharField(label='Логин', min_length=7, max_length=7,
                            widget=forms.TextInput(attrs={'placeholder': 'Введите логин'})
                            )
    password = forms.CharField(label='Пароль', min_length=10, max_length=15,
                               widget=forms.TextInput(attrs={'placeholder': 'Введите пароль'})
                               )