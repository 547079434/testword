from django.contrib import admin
from .models import *

# Register your models here.
class PointsHistoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'points', 'ip', 'create_at', 'update_at']
    search_fields = ['name','phone']
    list_filter = ['create_at','update_at']
admin.site.register(PointsHistory, PointsHistoryAdmin)


class PassWordsAdmin(admin.ModelAdmin):
    list_display = ['num', 'content']
admin.site.register(PassWords, PassWordsAdmin)