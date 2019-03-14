from django.conf.urls import include, url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views




router = routers.DefaultRouter()
router.register(r'icdapi', views.IcdcodeViewSet)


urlpatterns = [

 url(r'', include(router.urls)),

  
]
