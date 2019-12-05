from django.conf.urls import url, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'search'

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^get$', views.check_get, name='search_get'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
