from rest_framework import serializers

from django.contrib.auth import get_user_model

from user.models import UserMain
from character.models import Equipment, Character, CharacterEquipment
from contants import NAME_LENGHT, PASSWORD_LENGTH, USER_LENGTH, USER_VALIDATORS, EQUIPMENT

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    username = serializers.RegexField(
        regex=r'^[\w.@+-]+$',
        max_length=USER_LENGTH,
        required=True,
    )
    password = serializers.CharField(write_only=True, 
                                       style={'input_type': 'password'},
                                       max_length=PASSWORD_LENGTH,
                                       label='Пароль')
    password_2 = serializers.CharField(write_only=True,
                                     style={'input_type': 'password'},
                                     max_length=PASSWORD_LENGTH,
                                     label='Повторите пароль')
    first_name = serializers.CharField(max_length=NAME_LENGHT)
    last_name = serializers.CharField(max_length=NAME_LENGHT)
    
    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password',
            'password_2',
            'first_name',
            'last_name',
        ]
    
    def validate_username(self, username):
        if UserMain.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {'ERROR': USER_VALIDATORS['username']})
        return username
    
    def validate(self, data):
        if data['password'] != data['password_2']:
            raise serializers.ValidationError(
                {'ERROR': USER_VALIDATORS['password']}
            )
        return data 

    def create(self, validated_data):
        user = UserMain.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
    

class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'first_name',
            'last_name'
        ]


class EquipmentSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices=Equipment.EQUIP_CHOICES)

    class Meta:
        model = Equipment
        fields = [
            'title',
            'description', 
            'type',
            'bonus_strenght',
            'bonus_intelegence', 
            'bonus_agility',
            'bonus_wisdom'
        ]


class CharacterSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Character
        fields = [
            'user',
            'user_info',
            'title',
            'description',
            'type',
            'strenght',
            'intelegence',
            'agility',
            'wisdom'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserRetrieveSerializer(instance=instance.user, context=self.context).data
        return representation


class CharacterEquipmentSerializer(serializers.ModelSerializer):
    character = serializers.PrimaryKeyRelatedField(queryset=Character.objects.all())
    hands = serializers.PrimaryKeyRelatedField(queryset=Equipment.objects.all())
    chest = serializers.PrimaryKeyRelatedField(queryset=Equipment.objects.all())
    legs = serializers.PrimaryKeyRelatedField(queryset=Equipment.objects.all())
    weapon = serializers.PrimaryKeyRelatedField(queryset=Equipment.objects.all())

    class Meta:
        model = CharacterEquipment
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['hands'] = EquipmentSerializer(instance=instance.hands, context=self.context).data
        representation['chest'] = EquipmentSerializer(instance=instance.chest, context=self.context).data
        representation['legs'] = EquipmentSerializer(instance=instance.legs, context=self.context).data
        representation['weapon'] = EquipmentSerializer(instance=instance.weapon, context=self.context).data
        return representation