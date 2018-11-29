# coding=utf-8
from django.db import models

class PointsHistory(models.Model):
    name = models.CharField(verbose_name=u'姓名', max_length=50)
    phone = models.CharField(verbose_name=u'电话', max_length=50)
    points = models.IntegerField(u'字数',blank=True,null=True)
    ip = models.CharField(verbose_name=u'IP', max_length=100)
    content = models.TextField(u'每关分数',blank=True,null=True)
    create_at = models.DateTimeField(u'创建时间', auto_now_add=True)
    update_at = models.DateTimeField(u'更新时间', auto_now=True)

    class Meta:
        verbose_name = u'分数记录'
        verbose_name_plural = u'分数记录管理'

    def __unicode__(self):
        return '%s' % (self.name)

class PassWords(models.Model):
    num = models.IntegerField(u'关卡')
    content = models.TextField(u'本关字集',help_text='每个字之间用,(英文逗号)隔开')

    class Meta:
        verbose_name = u'关卡字集'
        verbose_name_plural = u'关卡字集管理'

    def __unicode__(self):
        return '%s' % (self.num)