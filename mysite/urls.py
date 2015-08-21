from django.conf.urls import include, url
#from django.conf.urls.defaults import *
from django.contrib import admin
from gigapp.views import hello
from gigapp.views import watstime
from gigapp.views import time_shift
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('^hello/$', hello),
    url('^watstime/$', watstime),
    url(r'^time/plus/(\d{1,2})/$', time_shift),
]
