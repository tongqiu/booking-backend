from django.contrib.auth.models import User, Group
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.serializers.serializer_user import UserCreateSerializer

class UserCreateView(generics.CreateAPIView):
    """
    Register new user, returns the user id and the auth token
    """
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        return Response(
            {
                'token': token.key,
                'id':serializer.instance.id,
                'username': serializer.instance.username,
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )

# https://github.com/Tivix/django-rest-auth/blob/master/rest_auth/urls.py
