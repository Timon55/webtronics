from rest_framework import serializers
from .models import Profile, Post
from likes import services as likes_services
from django.contrib.auth.models import User

class userProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            'user',
            'total_likes'
        )

    def get_is_fan(self, obj) -> bool:
        """Проверяет, лайкнул ли `request.user` пост (`obj`).
        """
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)