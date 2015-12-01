from django.conf.urls import include, url
from django.contrib import admin
from tastypie.api import Api
from main.api import UrlResource, ResultResource

v1_api = Api(api_name='v1')
v1_api.register(UrlResource())
v1_api.register(ResultResource())


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'^', include('main.urls')),
]
