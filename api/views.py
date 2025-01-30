from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action


from character.models import Character, Equipment, CharacterEquipment, Inventory
from quest.models import Quest, UserQuest
from api.serializers import (CharacterSerializer, CharacterEquipmentSerializer, EquipmentSerializer,
                             InvetorySerializer, QuestSerializer, UserQuestSerializer)
from api.permissions import IsAuthor
from contants import USER_QUEST


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


class QuestViewSet(viewsets.ModelViewSet):
    queryset = Quest.objects.all()
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['get', 'post']

    def get_serializer_class(self):
        if self.action == 'take_quest':
            return UserQuestSerializer
        return QuestSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @action(detail=True, methods=['post'], url_path='take_quest')
    def take_quest(self, request, pk):
        user = request.user
        quest = get_object_or_404(Quest, pk=pk)

        if UserQuest.objects.filter(user=user, quest=quest).exists():
            return Response(USER_QUEST['exists'], status=status.HTTP_400_BAD_REQUEST)

        user_quest = UserQuest.objects.create(user=user, quest=quest)
        serializer = self.get_serializer_class()(user_quest)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
