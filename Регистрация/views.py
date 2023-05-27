from rest_framework.views import APIView
from rest_framework.response import Response
from Регистрация.models import DjandoRegistration
from Регистрация.serializers import TeacherSerializer


class EntranceApiView(APIView):
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            login = serializer.validated_data['login']
            password = serializer.validated_data['password']
            try:
                DjandoRegistration.objects.get(login=login, password=password)
                return Response({'message': 'Пользователь найден'}, status=200)
            except DjandoRegistration.DoesNotExist:
                return Response({'message': 'Пользователь не найден'}, status=404)
        else:
            return Response({'message': 'Невалидные данные'}, status=400)
