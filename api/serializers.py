from rest_framework import serializers

from django.contrib.auth import get_user_model

from user.models import UserMain
from contants import NAME_LENGHT, PASSWORD_LENGTH, USER_LENGTH, USER_VALIDATORS

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    username = serializers.RegexField(
        regex=r'^[\w.@+-]+$',
        max_length=USER_LENGTH,
        required=True,
    )
    password = serializers.CharField(write_only=True, 
                                       style={'input_type': 'password'},
                                       label='Пароль')
    password_2 = serializers.CharField(write_only=True,
                                     style={'input_type': 'password'},
                                     label='Повторите пароль')
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