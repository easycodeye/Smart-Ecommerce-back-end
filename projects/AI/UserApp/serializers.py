from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.models import User

from UserApp.models import BirthDate, UserType


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        label='username',
        style={'input_type', 'email'}
    )
    password = serializers.CharField(
        style={'input_type', 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong email or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "email" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs


class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)


class BirthDateSerializer(serializers.Serializer):
    class Meta:
        model = BirthDate
        fields = '__all__'


class UserTypeSerializer(serializers.Serializer):
    class Meta:
        model = UserType
        fields = '__all__'
