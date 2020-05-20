from django import forms
from .models import Report, ProblemReported
class ReportForm(forms.ModelForm):
    
    class Meta:
        model = Report
        # fields = '__all__' # all fields
        exclude = ('user', 'production_line', ) 

class ProblemReportedForm(forms.ModelForm):
    
    class Meta: 
        model = ProblemReported  # 創建model
        # fields = '__all__' # all fields
        exclude = ('user', 'report', ) # 'user', 'report' 兩者不顯示

