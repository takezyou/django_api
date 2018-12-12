from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

from api.serializers import UserSerializer
from api.models import User


class SignUpView(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
