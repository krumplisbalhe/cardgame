from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cards/', include('playcards.urls')),
    url(r'^$', views.homepage),
    url(r'^accounts/', include('accounts.urls'))
]

urlpatterns += staticfiles_urlpatterns()
