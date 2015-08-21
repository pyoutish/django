from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def hello(request):
    return HttpResponse('WTF man?')

def watstime(request):
    curtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    html = "<html><body>It is now %s.</body></html>" % curtime
    return HttpResponse(html)

def time_shift(request, hour):
    try:
        int(hour)
    except ValueError:
        raise Http404()
    dt = str(datetime.datetime.now()) + ' And now try to add your %s hours by yourself smartie' % hour
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (hour, dt)
    return HttpResponse(html)
