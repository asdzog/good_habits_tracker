from rest_framework import serializers
from users.models import User
from users.validators import ChatIDValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name",  "email", "password", "telegram_chat_id"]
        validators = [ChatIDValidator(chat_id_field='telegram_chat_id'),]

    def create(self, validated_data):
        user = User(email=validated_data["email"])
        user.is_active = True
        user.set_password(validated_data["password"])
        user.save()
        return user
