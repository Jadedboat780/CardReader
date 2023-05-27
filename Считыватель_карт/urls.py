from django.contrib import admin
from django.urls import path, include
from Регистрация.views import EntranceApiView
from Таблица_посещаемости.views import TableApiView

urlpatterns = [
    path('admin_kalabok_36', admin.site.urls),
    path('', include('Считыватель_карт.rest-api')),
    path('rest-api/entrance', EntranceApiView.as_view(), name='register'),
    path('rest-api/couple', TableApiView.as_view(), name='table'),
]
