from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserCreateSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True}
        }

    def validate_email(self, value):
        if '@' not in value or '.' not in value:
            raise serializers.ValidationError('Email address is not valid')
        existing = User.objects.filter(email=value).first()
        if existing:
            raise serializers.ValidationError('Someone has already registered with that email address')
        return value

    def validate(self, data):
        if len(data.get('password', '')) < 6:
            raise serializers.ValidationError('Password must be at least 6 characters long')
        if data.get('password') != data.get('password2'):
            raise serializers.ValidationError('Passwords do not match')
        return data

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
