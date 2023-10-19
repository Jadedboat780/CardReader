from django.contrib import admin
from django.urls import path
from Registration.views import index
from TableCouples.views import table

urlpatterns = [
    path('admin_card/', admin.site.urls),
    path('', index),
    path('table/', table)
    # path('rest-api/entrance', EntranceApiView.as_view(), name='register'),
    # path('rest-api/couple', TableApiView.as_view(), name='table'),
]
