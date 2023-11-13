from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer


User = get_user_model()

class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')

        User.objects.create_user(username=username, password=password)
        return Response({'success': True})


class UsersListAPIView(APIView):
    def get(self, request):
        queryset = User.objects.all().values('username', 'first_name', 'last_name', 'email')
        serialized = UserSerializer(queryset, many=True)
        return Response(status=200, data=serialized.data)