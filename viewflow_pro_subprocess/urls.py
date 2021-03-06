from django.views import generic
from django.conf.urls import url, include
from django.contrib import admin
from material.frontend import urls as frontend_urls

urlpatterns = [
    url(r'^$', generic.RedirectView.as_view(url='/viewflow/', permanent=False)),
    url(r'^admin/', admin.site.urls),
    url(r'', include(frontend_urls)),
]
