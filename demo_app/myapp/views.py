from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import render


@api_view(['POST'])
def login_view(request):
	email = request.data.get('email')
	password = request.data.get('password')
	user = authenticate(request, username=email, password=password)
	if user is not None:
		return JsonResponse({'message': 'Login successful'}, status=200)
	else:
		return JsonResponse({'message': 'Invalid credentials'}, status=400)
	
def index(request):
    return render(request, 'index.html')