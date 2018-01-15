#_*_ encoding:utf-8 _*_
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import View,TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'