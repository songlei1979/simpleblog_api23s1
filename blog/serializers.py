from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'author']

class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'token']
        # fields = "__all__"

        extra_kwargs = {'password':{
            'write_only': True,
            'required': True
        }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        token = Token.objects.create(user=user)
        return user

    def get_token(self, obj):
        try:
            token = Token.objects.get(user=obj)
            print(token.__dict__["key"])
            return token.__dict__["key"]
        except Token.DoesNotExist:
            return None
