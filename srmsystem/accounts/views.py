from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .serializers import ClientSerializer


class RegisterApiView(APIView):
    """Функция регистрации пользователей"""

    def post(self, request: Request) -> Response:
        print(request.data)
        serializer = ClientSerializer()
        return Response(serializer.data, template_name="templates_only/login.html",  status=status.HTTP_200_OK)
