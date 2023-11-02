from django.contrib import admin
from django.urls import path
from Registration.views import Registration
from TableCouples.views import Table

urlpatterns = [
    path('admin_card/', admin.site.urls),
    path('', Registration.as_view()),
    path('table/', Table.as_view()),
    # path('rest-api/entrance', EntranceApiView.as_view(), name='register'),
    # path('rest-api/couple', TableApiView.as_view(), name='table'),
]
