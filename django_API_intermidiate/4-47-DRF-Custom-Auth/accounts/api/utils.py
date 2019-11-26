import datetime
from django.conf import settings
from django.utils import timezone

# Creating a new token manually
from rest_framework_jwt.settings import api_settings



expire_delta                    = api_settings.JWT_REFRESH_EXPIRATION_DELTA
# expire_delta = settings.JWT_AUTH['JWT_REFRESH_EXPIRATION_DELTA']    # JWT_REFRESH_EXPIRATION_DELTA

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': user.username,   # UserSerializer(user, context={'request': request}).data
        'expires': timezone.now() + expire_delta - datetime.timedelta(seconds=200)
    }