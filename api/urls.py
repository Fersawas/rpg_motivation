from django.urls import path, re_path, include

from rest_framework.routers import SimpleRouter


router = SimpleRouter()


urlpatterns = [
    re_path('^auth/', include('djoser.urls')),
    re_path('^auth/', include('djoser.urls.authtoken')),
]
