from django.contrib import admin
from django.urls import path, include
from Регистрация.views import EntranceApiView
from Таблица_посещаемости.views import TableApiView

urlpatterns = [
    path('************', admin.site.urls),
    path('', include('Считыватель_карт.rest-api')),
    path('******', EntranceApiView.as_view(), name='register'),
    path('**************', TableApiView.as_view(), name='table'),
]
