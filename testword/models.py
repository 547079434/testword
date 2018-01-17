# coding=utf-8
from django.db import models

class PointsHistory(models.Model):
    name = models.CharField(verbose_name=u'姓名', max_length=50)
    phone = models.CharField(verbose_name=u'电话', max_length=50)
    points = models.IntegerField(u'分数')
    ip = models.CharField(verbose_name=u'IP', max_length=100)
    create_at = models.DateTimeField(u'创建时间', auto_now_add=True)

    class Meta:
        verbose_name = u'分数记录'
        verbose_name_plural = u'分数记录管理'

    def __unicode__(self):
        return '%s' % (self.name)