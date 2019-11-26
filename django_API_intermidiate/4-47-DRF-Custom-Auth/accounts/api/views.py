from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response

# Permissions 
from rest_framework import permissions

# Creating a new token manually
from rest_framework_jwt.settings import api_settings

# Custom 
# from .utils import jwt_response_payload_handler

############  Copied from Creating a new token manually ##############
jwt_payload_handler             = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler              = api_settings.JWT_ENCODE_HANDLER
######################################################################

jwt_response_payload_handler    = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER



User = get_user_model()

class AuthView(APIView):
    permission_classes          = [permissions.AllowAny]        # [ IsAuthenticated, IsAuthenticatedOrReadOnly ]
    # authentication_classes      = []        # [ SessionAuthentication ]
    def post(self, request, *args, **kwargs):
        print(request.user)
        if request.user.is_authenticated:
            # print("User is authenticated")
            return Response({"detail": "You are already authenticated"}, status=400)
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        print(user)

        qs = User.objects.filter(
            Q(username__iexact=username) | 
            Q(email__iexact=username)
        ).distinct()
        if qs.count() == 1:
            user_obj = qs.first()
            if user_obj.check_password(password):
                user = user_obj
        
                payload = jwt_payload_handler(user)
                # payload = jwt_response_payload_handler(user)
                token = jwt_encode_handler(payload)
                response = jwt_response_payload_handler(token, user, request=request)

                # return Response({'token': token})
                return Response(response)
        return Response({"detail": "Invalid credentials"}, status=401) 
