from django.shortcuts import render, redirect
from Регистрация.models import DjandoRegistration
from Регистрация.form import RegisterForm


def home(request):
    form = RegisterForm
    if request.method == 'GET':
        return render(request, "index.html", context={'form': form})

    if request.method == 'POST':
        data = request.POST
        register_form = RegisterForm(data)
        if register_form.is_valid():
            login = register_form.cleaned_data['login']
            password = register_form.cleaned_data['password']
            data = DjandoRegistration.objects.filter(login=login, password=password).exists()

            if data:
                return redirect('/table/')
            else:
                return render(request, "index.html", context={'form': form})