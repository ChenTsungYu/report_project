"""
on_delete=models.CASCADE 參考下方文章的說明
https://ithelp.ithome.com.tw/articles/10200181

auto_now 與auto_now_add 的比較
https://www.jianshu.com/p/74d02fddc691、 https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.DateTimeField

verbose_name、verbose_name_plural
https://www.cnblogs.com/feixuelove1009/p/8419493.html
"""
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from products.models import Product
from areas.models import ProductionLine
from categories.models import Category
from django.urls import reverse
import random
# Create your models here.

# hours= (   # here is sample of hours
#     ("1", "1"),
#     ("2", "2"),
#     ("3", "3"),
#     ...
# )
hours = ([(str(x), str(x)) for x in range(1, 25)])
el = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
     'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

class Report(models.Model):
    day = models.DateField(default=timezone.now)
    start_hour = models.CharField(max_length=2, choices=hours)
    end_hour = models.CharField(max_length=2, choices=hours)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    plan = models.PositiveIntegerField() # 正數
    execution = models.PositiveIntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    production_line = models.ForeignKey(ProductionLine, on_delete=models.CASCADE)

    def get_day(self):
        return self.day.strftime('%Y/%m/%d')
    def get_absolute_url(self): #  常用於定義 detailView
        return reverse("reports:update-view", kwargs={'production_line': self.production_line, 'pk': self.pk, })
    def __str__(self): # 在後台顯示的Object名稱
        # return f"{self.start_hour}-{self.end_hour}-{self.production_line}"
        return "{}-{}-{}".format(self.start_hour, self.end_hour, self.production_line)
    
    class Meta:
        ordering = ('-created', ) # 依照建立時間排序，"-"表 reverse

def random_code(): # 給予problemID隨機產生的值
    random.shuffle(el)
    code = [str(x) for x in el[:12]]
    str_code = ''.join(code)

    return str_code
class ProblemReported(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    problem_id = models.CharField(max_length=12, unique=True, blank=True, default=random_code)
    breakdown = models.PositiveIntegerField()
    public = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}-{}".format(self.category.name, self.description[:20])
    
    class Meta:
        verbose_name = "Problem Reported"
        verbose_name_plural = "Problems Reported"