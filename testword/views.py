from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import View,TemplateView
from django.shortcuts import render
from .settings import BASE_DIR
from .models import PointsHistory,PassWords
import random

# def get_words():
#     words = []
#     with open(BASE_DIR.replace('\\','/')+'/testword/medias/words.txt','r') as w:
#         words = w.read().split(',')
#         print(len(words))
#         words = [i for i in words if i]
#         print(len(words))
#     return words

# WORDS = get_words()
def get_words_list():
    WORDS_1 = random.sample(PassWords.objects.get(num=1).content.split(','),150)
    WORDS_2 = random.sample(PassWords.objects.get(num=2).content.split(','),150)
    WORDS_3 = random.sample(PassWords.objects.get(num=3).content.split(','),150)
    WORDS_4 = random.sample(PassWords.objects.get(num=4).content.split(','),150)
    WORDS_LIST = [WORDS_1,WORDS_2,WORDS_3,WORDS_4]
    return WORDS_LIST

class IndexView(TemplateView):
    template_name = 'index.html'

    def post(self,request):
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip =  request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        name = request.POST.get('name','')
        phone = request.POST.get('phone','')
        history = PointsHistory.objects.filter(phone=phone)
        page = 1
        checknum = 0
        passnum = 1
        points = 0
        if not history.count():
            PointsHistory.objects.create(name=name,phone=phone,ip=ip)
        else:
            content = history[0].content
            if content:
                data = eval(content)
                page = data['page']
                checknum = data['checknum']
                passnum = data['passnum']
                points = history[0].points
        if points:
            url = '/end/?name='+name+'&phone='+phone+'&checknum='+str(checknum)
        else:
            url = '/words/?name='+name+'&phone='+phone+'&page='+str(page)+'&checknum='+str(checknum)+'&passnum='+str(passnum)
        return HttpResponse(url)


class WordsView(TemplateView):
    template_name = 'words.html'

    def get_context_data(self, **kwargs):
        context = super(WordsView, self).get_context_data()
        name = self.request.GET.get('name','')
        phone = self.request.GET.get('phone','')
        page = int(self.request.GET.get('page',1))
        checknum = int(self.request.GET.get('checknum',0))
        passnum = self.request.GET.get('passnum',1)

        WORDS_LIST = get_words_list()
        words = WORDS_LIST[int(passnum)-1]
        num,left = divmod(len(words),10)
        if left > 0:
            num += 1
        words = words[(int(page)-1)*10:(int(page))*10]

        content_dict = {'page':page,'checknum':checknum,'passnum':passnum}
        history = PointsHistory.objects.filter(phone=phone)
        if history.count():
            history = history[0]
            history.content = str(content_dict)
            history.save()
        context.update({
            'page':page,
            'words':words,
            'checknum':int(checknum),
            'name':name,
            'phone':phone,
            'passnum':passnum,
            'num':num
        })
        return context

class EndView(TemplateView):
    template_name = 'end.html'

    def get_context_data(self, **kwargs):
        context = super(EndView, self).get_context_data()

        name = self.request.GET.get('name','')
        phone = self.request.GET.get('phone','')
        checknum = self.request.GET.get('checknum',0)
        # WORDS_LIST = get_words_list()
        # total = sum([len(i) for i in WORDS_LIST])
        # points = int(int(checknum)/total*100)
        points = checknum
        history = PointsHistory.objects.filter(phone=phone)
        if history.count():
            history = history[0]
            history.points = points
            history.save()
        context.update({
            'points':points,
            'name':name,
            'phone':phone
        })
        return context


class AgainView(View):
    def post(self,request):
        phone = request.POST.get('phone','')
        name = request.POST.get('name','')
        history = PointsHistory.objects.filter(phone=phone)
        if history.count():
            history = history[0]
            history.points = None
            history.content = ''
            history.save()
        return HttpResponse('ok')