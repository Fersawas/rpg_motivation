from django.urls import path, re_path, include

from rest_framework.routers import SimpleRouter

from api.views import CharacterEquipmentViewSet


router = SimpleRouter()

router.register('character', CharacterEquipmentViewSet, 'character')

urlpatterns = [
    path('', include(router.urls)),
    re_path('^auth/', include('djoser.urls')),
    re_path('^auth/', include('djoser.urls.authtoken')),
]
