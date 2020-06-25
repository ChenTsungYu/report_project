"""
get_object_or_404
https://ithelp.ithome.com.tw/articles/10203801
https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/

HTTP_REFERER
https://docs.djangoproject.com/en/3.0/ref/request-response/

UpdateView
https://www.itdaan.com/tw/24b192b32828b0917f8eb391bed96d6c

UpdateView 的相關討論: 
Why can you import UpdateView in “multiple ways”
https://stackoverflow.com/questions/54052554/why-can-you-import-updateview-in-multiple-ways
"""
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReportForm, ProblemReportedForm
from .models import Report
from areas.models import ProductionLine
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, FormView
# Create your views here.

class HomeView(FormView):
    template_name = 'reports/home.html'
    form_class = ReportSelectLineForm

class ReportUpdateView(UpdateView):
    model = Report
    form_class = ReportForm
    template_name = 'reports/update.html'
    def get_success_url(self):
        return self.request.path

@login_required
def delete_view(request, *args, **kwargs):
    # get report id
    r_id = kwargs.get("pk")
    obj = Report.objects.get(id=r_id)
    obj.delete()
    return redirect(request.META.get('HTTP_REFERER')) # redirect to current view

@login_required # 要求要是登入的狀態
def report_view(request, production_line):
    form = ReportForm(request.POST or None, production_line=production_line)
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
            # form = ReportForm() # restart 
            # pform = ProblemReportedForm()
            return redirect(request.META.get('HTTP_REFERER')) # 提交表單時，回到當前頁面

    elif "submitProblemBtn" in request.POST:
        if form.is_valid():  
            obj = form.save(commit=False)
            obj.user = request.user
            obj.production_line = line
            obj.save()
            # form = ReportForm() 
            # pform = ProblemReportedForm() # restart
            return redirect(request.META.get('HTTP_REFERER')) # 提交表單時，回到當前頁面
    context = {
         "form": form,
         "pform": pform,
         "object_list": queryset,
     }

    return render(request, 'reports/report.html', context)

