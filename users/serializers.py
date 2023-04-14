from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(
        max_length=150,
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="username already taken."
            )
        ],
    )
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="email already registered."
            )
        ],
    )
    password = serializers.CharField(required=True, write_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateTimeField(required=False)
    is_employee = serializers.BooleanField(default=False, required=False)
    is_superuser = serializers.ReadOnlyField()

    def create(self, validated_data: dict):
        if validated_data["is_employee"] == True:
            return User.objects.create_superuser(**validated_data)
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        if "password" in validated_data:
            new_password = validated_data.pop("password")
            instance.set_password(new_password)

        instance.save()
        return instance


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, required=True)
    password = serializers.CharField(required=True, write_only=True)
