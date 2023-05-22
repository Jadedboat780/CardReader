from django.contrib import admin
from django.urls import path, include
from Таблица_посещаемости.views import MyView


urlpatterns = [
    path('admin_kalabok_36', admin.site.urls),
    path('', include('Таблица_посещаемости.urls')),
    path('rest-api/couple', MyView.as_view(), name='table'),
]

# handler404 = "Считыватель_карт.views.error_404"
