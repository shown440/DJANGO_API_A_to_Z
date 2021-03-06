import datetime

from django.contrib.auth import get_user_model
from django.utils import timezone

from rest_framework import serializers

# Creating a new token manually
from rest_framework_jwt.settings import api_settings


############  Copied from Creating a new token manually ##############
jwt_payload_handler             = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler              = api_settings.JWT_ENCODE_HANDLER
######################################################################

jwt_response_payload_handler    = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

expire_delta                    = api_settings.JWT_REFRESH_EXPIRATION_DELTA



User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    password             = serializers.CharField(style={"input_type": "password"}, write_only=True)
    password2            = serializers.CharField(style={"input_type": "password"}, write_only=True)
    # Now will get token
    token                = serializers.SerializerMethodField(read_only=True)  # read_only=True
    expires              = serializers.SerializerMethodField(read_only=True)
    # token_response       = serializers.SerializerMethodField(read_only=True)
    message              = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
            'token',
            'expires',
            # 'token_response',

            'message',

        ]
        # extra_kwargs = {"password": {"write_only": True}}

    def get_message(self, obj):
        return "Thankyou for registering. Please verify your email before continuing."

    # def validate_email(self, value):
    #     qs              = User.objects.filter(email__iexact=value)
    #     if qs.exists:
    #         raise serializers.ValidationError("User with this email is already exists.")
    #     return value
    
    # def validate_email(self, value):
    #     qs              = User.objects.filter(username__iexact=value)
    #     if qs.exists:
    #         raise serializers.ValidationError("User with this username is already exists.")
    #     return value


    # # this part is no need part, used to just for practise
    # def get_token_response(self, obj):
    #     user            = obj
    #     payload         = jwt_payload_handler(user)
    #     # payload         = jwt_response_payload_handler(user)
    #     token           = jwt_encode_handler(payload)
    #     context         = self.context
    #     request         = context['request']
    #     print("===============>", request.user.is_authenticated)
    #     response        = jwt_response_payload_handler(token, user, request=context['request'])
    #     return response

    def get_token(self, obj):   # Instance of the model 
        user            = obj
        payload         = jwt_payload_handler(user)
        # payload         = jwt_response_payload_handler(user)
        token           = jwt_encode_handler(payload)
        return token
    
    def get_expires(self, obj):
        return timezone.now() + expire_delta - datetime.timedelta(seconds=200)

    def validate(self, data):
        pw              = data.get("password")
        # pw2             = data.get("password2")
        pw2             = data.pop("password2")

        if pw != pw2:
            raise serializers.ValidationError("Password must match")
        return data
    
    def create(self, validated_data):
        # print(validated_data)
        username        = validated_data.get("username")
        email           = validated_data.get("email")
        password        = validated_data.get("password")

        # user_obj = User.objects.create(username=username, email=email)
        user_obj = User(username=username, email=email)
        user_obj.set_password(password)
        user_obj.is_active = False
        user_obj.save()
        return user_obj

