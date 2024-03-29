from __future__ import unicode_literals
from django.db import models


# Create your models here.

class Student(models.Model):
    SEX_ITEMS = [
        (1, '男'),
        (2, '女'),
        (3, '未知')
    ]
    STATUS_ITEMS = [
        (0, '申请'),
        (1, '通过'),
        (2, '拒绝')
    ]

    name = models.CharField(max_length=128, verbose_name="姓名")
    sex = models.IntegerField(choices=SEX_ITEMS, verbose_name="性别")
    profession = models.CharField(max_length=128, verbose_name="职业")
    email = models.EmailField(verbose_name="邮箱")
    qq = models.CharField(max_length=128, verbose_name="QQ")
    phone = models.CharField(max_length=128, verbose_name="电话")

    status = models.IntegerField(choices=STATUS_ITEMS, verbose_name="审核状态", default=0)

    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="创建时间")

    def __str__(self):
        return f'Student: {self.name}'

    @classmethod
    def get_all(cls):
        return cls.objects.all()


class Meta:
    verbose_name = verbose_name_plural = "学员信息"
