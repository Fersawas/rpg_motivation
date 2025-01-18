from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, AllowAny
from rest_framework.response import Response

from character.models import Character, Equipment, CharacterEquipment
from api.serializers import CharacterSerializer, CharacterEquipmentSerializer, EquipmentSerializer


User = get_user_model()


class CharacterEquipmentViewSet(viewsets.ModelViewSet):
    serializer_class = CharacterEquipmentSerializer
    queryset = CharacterEquipment.objects.all()
