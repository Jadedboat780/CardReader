from django.contrib import admin
from django.urls import path, include
from Регистрация.views import home
from Таблица_посещаемости.views import table


urlpatterns = [
    path('************', admin.site.urls),
    path('rest-api', include('Таблица_посещаемости.urls')),
    path('', home, name='home'),
    path('table/', table, name='table'),
]

handler404 = "Считыватель_карт.views.error_404"
