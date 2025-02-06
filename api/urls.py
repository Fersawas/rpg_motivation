from django.urls import path, re_path, include

from rest_framework.routers import SimpleRouter

from api.views import CharacterEquipmentViewSet, InvetoryViewSet, QuestViewSet


router = SimpleRouter()

router.register("character", CharacterEquipmentViewSet, "character")
router.register("inventory", InvetoryViewSet, "inventory")
router.register("quest", QuestViewSet, "quest")

urlpatterns = [
    path("", include(router.urls)),
    re_path("^auth/", include("djoser.urls")),
    re_path("^auth/", include("djoser.urls.authtoken")),
]
