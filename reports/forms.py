"""
Query model
https://medium.com/@andyludeveloper/%E7%8E%A9-django-part-6-%E6%9F%A5%E8%A9%A2%E8%B3%87%E6%96%99-query-model-af542ed8eb5e

"""
from django import forms
from .models import Report, ProblemReported
from django.shortcuts import get_object_or_404
from areas.models import ProductionLine
import logging as lgg
lgg.basicConfig(level=lgg.INFO)

class ReportSelectLineForm(forms.Form):
    production_line = forms.ModelChoiceField(queryset=ProductionLine.object.none())
    

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        # fields = '__all__' # all fields
        exclude = ('user', 'production_line', )

    def __init__(self, *args, **kwargs):
            production_line = kwargs.pop('production_line', None) # 從dic中刪除值並回傳被該值
            super().__init__(*args, **kwargs)
            if production_line != None: # 每次表單提交都是初始化
                line = get_object_or_404(ProductionLine, name=production_line)
                lgg.debug(line.name)
                self.fields["product"].queryset = line.products.all()
class ProblemReportedForm(forms.ModelForm):
    
    class Meta: 
        model = ProblemReported  # 創建model
        # fields = '__all__' # all fields
        exclude = ('user', 'report', 'problem_id') # 'user', 'report' 兩者不顯示

