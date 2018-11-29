from django.http import HttpResponseRedirect
from django.contrib import admin
from .models import *
from .settings import BASE_DIR
import xlwt

# Register your models here.
def export_data(modeladmin, request, queryset):
    url = '/medias/export.xls'
    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('sheet1')
    ws.write(0, 0, '姓名')
    ws.write(0, 1, '电话')
    ws.write(0, 2, '分数')
    ws.write(0, 3, 'IP')
    ws.write(0, 4, '创建时间')
    ws.write(0, 5, '更新时间')
    for i,q in enumerate(queryset):
        ws.write(i+1, 0, q.name)
        ws.write(i+1, 1, q.phone)
        ws.write(i+1, 2, q.points)
        ws.write(i+1, 3, q.ip)
        ws.write(i+1, 4, q.create_at.strftime("%Y-%m-%d %H:%M:%S"))
        ws.write(i+1, 5, q.update_at.strftime("%Y-%m-%d %H:%M:%S"))
    wb.save(BASE_DIR+'/testword'+url)
    return HttpResponseRedirect(url)
export_data.short_description = "导出EXCEL"

class PointsHistoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'points', 'ip', 'create_at', 'update_at']
    search_fields = ['name','phone']
    list_filter = ['create_at','update_at']
    actions = [export_data]
admin.site.register(PointsHistory, PointsHistoryAdmin)


class PassWordsAdmin(admin.ModelAdmin):
    list_display = ['num', 'content']
admin.site.register(PassWords, PassWordsAdmin)