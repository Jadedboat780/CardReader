from django.contrib import admin
from django.urls import path, include
from Registration.views import EntranceApiView
from TableCouples.views import TableApiView

urlpatterns = [
    path('admin_card/', admin.site.urls),
    path('', include('CardReader.rest-api')),
    path('rest-api/entrance', EntranceApiView.as_view(), name='register'),
    path('rest-api/couple', TableApiView.as_view(), name='table'),
]
