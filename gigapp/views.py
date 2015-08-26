from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.shortcuts import render_to_response
# Create your views here.

def hello(request):
    return HttpResponse('WTF man?')

def watstime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    c = Context({'current_date': now})
    html = t.render(c)
    return HttpResponse(html)



def time_shift(request, hour):
    try:
        int(hour)
    except ValueError:
        raise Http404()
    dt = str(datetime.datetime.now()) + ' And now try to add your %s hours by yourself smartie' % hour
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (hour, dt)
    return HttpResponse(html)

def funny(request):
    return render_to_response('funny_fun.html', {'name':'Josh', 'surname': 'Smith'})