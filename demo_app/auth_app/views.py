from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging
import psycopg2
from psycopg2 import sql
from django.contrib.auth.hashers import check_password

# Set up logging
logger = logging.getLogger(__name__)

@csrf_exempt
def login_view(request):
	if request.method == 'POST':
		try:
			data = json.loads(request.body)
			username = data.get('username')
			password = data.get('password')
			
			# Log the username and password
			logger.info(f"Username: {username}, Password: {password}")
			
			# Authenticate the user
			user = custom_authenticate(username, password)
			
			if user is not None:
				# Authentication successful
				logger.info(f"Authentication successful for user: {username}")
				return JsonResponse({'success': True})
			else:
				# Authentication failed
				logger.info(f"Authentication failed for user: {username}")
				return JsonResponse({'success': False, 'error': 'Invalid credentials'}, status=401)
		except json.JSONDecodeError:
			logger.error("Invalid JSON received")
			return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)
	logger.error("Invalid request method")
	return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)

def custom_authenticate(username, password):
	try:
		# Connect to PostgreSQL database
		logger.info("Connecting to PostgreSQL database")
		conn = psycopg2.connect(
			dbname="postgres",
			user="nishit",
			password="your_password",  # Ensure to replace 'your_password' with the actual password
			host="localhost"
		)
		cursor = conn.cursor()
		
		# Query to find the user
		logger.info(f"Executing query to find user: {username}")
		query = sql.SQL("SELECT password FROM users WHERE username = %s")
		cursor.execute(query, (username,))
		result = cursor.fetchone()
		
		if result:
			stored_password = result[0]
			logger.info(f"User found: {username}, verifying password")
			if check_password(password, stored_password):
				# Create a mock user object
				user = {
					'username': username,
					'password': stored_password
				}
				logger.info(f"Password verification successful for user: {username}")
				return user
			else:
				logger.info(f"Password verification failed for user: {username}")
		else:
			logger.info(f"User not found: {username}")
		
		cursor.close()
		conn.close()
	except Exception as e:
		logger.error(f"Error authenticating user: {e}")
		return None
	return None
# from django.contrib.auth.models import User
# from django.contrib.auth.hashers import check_password

# Set up logging
logger = logging.getLogger(__name__)

@csrf_exempt
def login_view(request):
	if request.method == 'POST':
		try:
			data = json.loads(request.body)
			username = data.get('username')
			password = data.get('password')
			
			# Log the username and password
			logger.info(f"Username: {username}, Password: {password}")
			
			# Authenticate the user
			user = custom_authenticate(username, password)
			
			if user is not None:
				# Authentication successful
				return JsonResponse({'success': True})
			else:
				# Authentication failed
				return JsonResponse({'success': False, 'error': 'Invalid credentials'}, status=401)
		except json.JSONDecodeError:
			return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)
	return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)

def custom_authenticate(username, password):
	try:
		# Connect to PostgreSQL database
		conn = psycopg2.connect(
			dbname="postgres",
			user="nishit",
			password="your_password",  # Ensure to replace 'your_password' with the actual password
			host="localhost"
		)
		cursor = conn.cursor()
		
		# Query to find the user
		query = sql.SQL("SELECT password FROM users WHERE username = %s")
		cursor.execute(query, (username,))
		result = cursor.fetchone()
		
		if result:
			stored_password = result[0]
			if check_password(password, stored_password):
				# Create a mock user object
				user = {
					'username': username,
					'password': stored_password
				}
				return user
		cursor.close()
		conn.close()
	except Exception as e:
		logger.error(f"Error authenticating user: {e}")
		return None
	return None

