from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db.transaction import atomic
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import Serializer, ModelSerializer


class RegistrationSerializer(Serializer):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    username = CharField(max_length=255)
    password = CharField(max_length=255)
    confirm_password = CharField(max_length=255, write_only=True)

    def validate(self, data):
        if User.objects.filter(username=data['username']).exists():
            raise ValidationError(f"This {data['username']} is already exists")

        if data['password'] != data['confirm_password']:
            raise ValidationError("Password didn't match")

        return data

    @atomic
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        validated_data['password'] = make_password(validated_data['password'])
        user = User(**validated_data)
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username')
