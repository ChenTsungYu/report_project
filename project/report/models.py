"""
on_delete=models.CASCADE 參考下方文章的說明
https://ithelp.ithome.com.tw/articles/10200181

auto_now 與auto_now_add 的比較
https://www.jianshu.com/p/74d02fddc691、 https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.DateTimeField
"""
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

# hours= (   # here is sample of hours
#     ("1", "1"),
#     ("2", "2"),
#     ("3", "3"),
#     ...
# )
hours = ([(str(x)), (str(x)) for i in range(1, 24)])
class Report(models.Model):
    day = models.DateField(default=timezone.now)
    start_hour = models.CharField(max_length=50, choices=hours)
    end_hour = models.CharField(max_length=50, choices=hours)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.PositiveIntegerField() # 正數
    execution = models.PositiveIntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # production_line = models.ForeignKey(ProductionLine, on_delete=models.CASCADE)
