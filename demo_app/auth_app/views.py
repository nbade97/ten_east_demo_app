import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import psycopg2
from psycopg2 import sql
from django.contrib.auth.hashers import check_password, make_password

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            
            # Log the username and password
            print(f"Username: {username}, Password: {password}")
            
            # Authenticate the user
            user = custom_authenticate(username, password)
            
            if user is not None:
                # Authentication successful
                print(f"Authentication successful for user: {username}")
                return JsonResponse({'success': True})
            else:
                # Authentication failed
                print(f"Authentication failed for user: {username}")
                return JsonResponse({'success': False, 'error': 'Invalid credentials'}, status=401)
        except json.JSONDecodeError:
            print("Invalid JSON received")
            return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)
    print("Invalid request method")
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)

def custom_authenticate(username, password):
    try:
        # Connect to PostgreSQL database
        print("Connecting to PostgreSQL database")
        conn = psycopg2.connect(
            dbname="postgres",
            user="nishit",
            host="localhost"
        )
        cursor = conn.cursor()
        
        # Query to find the user
        print(f"Executing query to find user: {username}")
        query = sql.SQL("SELECT password FROM users WHERE username = %s")
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        
        if result:
            print(f'checking result: {result}')
            stored_password = result[0]
            print(f"User found: {username}, verifying password")
            
            # print(f'hashed_password: {make_password(result[0])}')
            print(f'{check_password(password, stored_password)}')
            if check_password(password, stored_password):
                # Create a mock user object
                user = {
                    'username': username,
                    'password': stored_password
                }
                print(f"Password verification successful for user: {username}")
                return user
            else:
                print(f"Password verification failed for user: {username}")
        else:
            print(f"User not found: {username}")
        
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error authenticating user: {e}")
        return None
    return None

@csrf_exempt
def add_contribution(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = data.get('user')
            amount = data.get('amount')
            project_name = data.get('project_name')
            
            # Log the received data
            print(f"Received data - User: {user}, Amount: {amount}, Project Name: {project_name}")
            
            # Connect to PostgreSQL database
            print("Connecting to PostgreSQL database")
            conn = psycopg2.connect(
                dbname="postgres",
                user="nishit",
                host="localhost"
            )
            cursor = conn.cursor()
            
            # Insert the data into the contributions table
            query = sql.SQL("INSERT INTO contributions (user, amount, project_name, timestamp) VALUES (%s, %s, %s, %s)")
            cursor.execute(query, (user, amount, project_name, datetime.now()))
            conn.commit()
            
            print(f"Contribution added successfully for user: {user}")
            
            cursor.close()
            conn.close()
            
            return JsonResponse({'success': True})
        except json.JSONDecodeError:
            print("Invalid JSON received")
            return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            print(f"Error adding contribution: {e}")
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    print("Invalid request method")
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)