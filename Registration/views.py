from django.shortcuts import render, redirect
from rest_framework.views import APIView


class Registration(APIView):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        print(request.POST)
        return redirect('table/')
