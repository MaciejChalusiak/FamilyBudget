from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from User.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['password'] = make_password(data['password'])
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
