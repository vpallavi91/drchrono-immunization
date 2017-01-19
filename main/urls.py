from django.conf.urls import url,include
from django.contrib import admin
from views import intro,entry,trial

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^detail/$', intro,name = 'intro'),
    url(r'^(?P<id>\d+)/trial/$', trial,name='trial'),
    url(r'^$', entry)
]
