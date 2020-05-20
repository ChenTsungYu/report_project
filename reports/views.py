"""
get_object_or_404
https://ithelp.ithome.com.tw/articles/10203801
https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/
"""
from django.shortcuts import render, get_object_or_404
from .forms import ReportForm, ProblemReportedForm
from .models import Report
from areas.models import ProductionLine
# Create your views here.

def report_view(request, production_line):
    form = ReportForm(request.POST or None)
    pform = ProblemReportedForm(request.POST or None)
    # production_line__name 注意Report中的Foreign Key 為production_line
    queryset = Report.objects.filter(production_line__name=production_line)
    line = get_object_or_404(ProductionLine, name=production_line)

    if "ProblemModelBtn" in request.POST:
        rp_id = request.POST.get("report_id")
    # print("rp_id: ", rp_id)
        if pform.is_valid():
            report = Report.objects.get(id=rp_id)
            # print("data")
            obj = pform.save(commit=False)
            obj.user = request.user
            obj.report = report
            obj.save()
            form = ReportForm() # restart
            # pform = ProblemReportedForm()

    elif "submitProblemBtn" in request.POST:
        if form.is_valid():  
            obj = form.save(commit=False)
            obj.user = request.user
            obj.production_line = line
            obj.save()
            # form = ReportForm() 
            pform = ProblemReportedForm() # restart

    context = {
         "form": form,
         "pform": pform,
         "object_list": queryset,
     }

    return render(request, 'reports/report.html', context)

