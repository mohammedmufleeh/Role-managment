from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Role, Right, Member

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name')

class RightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Right
        fields = ('id', 'name')

class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    role = RoleSerializer()

    class Meta:
        model = Member
        fields = ('id', 'user', 'role')

class MemberCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Member
        fields = ('user', 'role')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(
            username=user_data['username'],
            email=user_data['email'],
            password=user_data['password']
        )
        member = Member.objects.create(user=user, **validated_data)
        return member

class MemberUpdateSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Member
        fields = ('id', 'user', 'role')
