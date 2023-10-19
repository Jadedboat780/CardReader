from django.shortcuts import render
from rest_framework.views import APIView



# class EntranceApiView(APIView):
#     def post(self, request):
#         serializer = TeacherSerializer(data=request.data)
#         if serializer.is_valid():
#             login = serializer.validated_data['login']
#             password = serializer.validated_data['password']
#             try:
#                 Registration.objects.get(login=login, password=password)
#                 return Response({'message': 'Пользователь найден'}, status=200)
#             except Registration.DoesNotExist:
#                 return Response({'message': 'Пользователь не найден'}, status=404)
#         else:
#             return Response({'message': 'Невалидные данные'}, status=400)


def index(request):
    return render(request, 'login.html')
