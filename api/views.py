from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action


from character.models import Character, Equipment, CharacterEquipment, Inventory
from api.serializers import CharacterSerializer, CharacterEquipmentSerializer, EquipmentSerializer, InvetorySerializer
from api.permissions import IsAuthor


User = get_user_model()


class CharacterEquipmentViewSet(viewsets.ModelViewSet):
    serializer_class = CharacterEquipmentSerializer
    queryset = CharacterEquipment.objects.all()
    permission_classes = [IsAuthor, IsAuthenticated]

    @action(detail=True, methods=['get'], url_path='equip')
    def equip(self, request, pk):
        pass


class InvetoryViewSet(viewsets.ModelViewSet):
    serializer_class = InvetorySerializer

    def get_queryset(self):
        user = self.request.user
        inventory = get_object_or_404(
                Inventory,
                character = user.character
            )
        return Inventory.objects.filter(pk=inventory.pk)
            