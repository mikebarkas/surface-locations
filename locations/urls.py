from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^state/', include('location_data.urls')),
    url(r'^', include('basic_pages.urls')),
]
