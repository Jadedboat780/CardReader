from django.contrib import admin
from django.urls import path
from Регистрация.views import home
from Таблица_посещаемости.views import table


urlpatterns = [
    path('***********', admin.site.urls),
    path('', home, name='home'),
    path('table/', table, name='table'),
]

handler404 = "Считыватель_карт.views.error_404"
