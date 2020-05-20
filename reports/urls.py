from django.urls import path
from.views import report_view

app_name = 'reports' # 對應app

urlpatterns = [
    path('<str:production_line>/', report_view, name="report-view")
]

