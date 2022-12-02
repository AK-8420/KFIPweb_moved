from django.views.generic import TemplateView
from django.http import HttpResponse

class TopView(TemplateView):
    template_name = 'top.html'


class GameView(TemplateView):
    template_name = 'games.html'


def WakeUP(request):
    return HttpResponse('<h1>Wake up Heroku server!!</h1>')
