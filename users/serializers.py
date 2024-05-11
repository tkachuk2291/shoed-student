from rest_framework import serializers
from users.models import Client
from users.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            "full_name",
            "speciality",
            "profile_description",
            "rating",
            "online_status",
            "last_activity",
            "image_url"
        )


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "online_status",
            "confirmation_of_payment",
            "full_name",
            "image_url",
            "last_activity",
        )


class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("id", "image_url")


class AuthorImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("id", "image_url")
