from django.conf.urls import url
from django.contrib import admin

from website.views import login, register, profile


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', login, name='login'),
    url(r'^$', register, name='register'),
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile')
]
