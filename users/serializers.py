from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from users.models import User
from users.validators import ChatIDValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password", "telegram_chat_id"]
        validators = [ChatIDValidator(chat_id_field='telegram_chat_id'),]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):

        raw_password = validated_data["password"]
        validated_data["password"] = make_password(raw_password)
        user = User(**validated_data)
        user.save()
        return user
