from django.shortcuts import render
from .forms import ReportForm, ProblemReportedForm
from .models import Report
# Create your views here.

def report_view(request, production_line):
    form = ReportForm()
    pform = ProblemReportedForm()
    # production_line__name 注意Report中的Foreign Key 為production_line
    queryset = Report.objects.filter(production_line__name=production_line)

    context = {
         "form": form,
         "pform": pform,
         "object_list": queryset,
     }

    return render(request, 'reports/report.html', context)

