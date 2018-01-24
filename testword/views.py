from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import View,TemplateView
from django.shortcuts import render
from .settings import BASE_DIR
from .models import PointsHistory

def get_words():
    words = []
    with open(BASE_DIR.replace('\\','/')+'/testword/medias/words.txt','r') as w:
        words = w.read().split(',')
        print(len(words))
        words = [i for i in words if i]
        print(len(words))
    return words

WORDS = get_words()

class IndexView(TemplateView):
    template_name = 'index.html'

class WordsView(TemplateView):
    template_name = 'words.html'

    def get_context_data(self, **kwargs):
        context = super(WordsView, self).get_context_data()
        name = self.request.GET.get('name','')
        phone = self.request.GET.get('phone','')
        page = self.request.GET.get('page',1)
        checknum = self.request.GET.get('checknum',0)

        num,left = divmod(len(WORDS),10)
        if left > 0:
            num += 1
        print(num)
        print(page)
        words = WORDS[(int(page)-1)*10:(int(page))*10]
        context.update({
            'page':page,
            'words':words,
            'checknum':int(checknum),
            'name':name,
            'phone':phone,
            'num':num
        })
        return context

class EndView(TemplateView):
    template_name = 'end.html'

    def get_context_data(self, **kwargs):
        context = super(EndView, self).get_context_data()
        if 'HTTP_X_FORWARDED_FOR' in self.request.META:
            ip =  self.request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = self.request.META['REMOTE_ADDR']

        name = self.request.GET.get('name','')
        phone = self.request.GET.get('phone','')
        checknum = self.request.GET.get('checknum',0)

        # points = '%.2f' % float(100*(int(checknum)/len(WORDS)))
        points = int(int(checknum)/len(WORDS)*100)
        # if name and phone:
        #     PointsHistory.objects.create(name=name,phone=phone,points=points)
        context.update({
            'points':points,
        })
        return context