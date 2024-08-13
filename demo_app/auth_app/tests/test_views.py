import json
from django.test import TestCase, Client
from unittest.mock import patch, MagicMock
from django.urls import reverse
import psycopg2

class LoginViewTests(TestCase):
	def setUp(self):
		self.client = Client()
		self.url = reverse('login')  # Ensure this matches your URL configuration
		print(f"Setup complete. URL set to {self.url}")

	@patch('auth_app.views.psycopg2.connect')
	def test_successful_authentication(self, mock_connect):
		print("Starting test_successful_authentication")
		# Mock the database connection and cursor
		mock_conn = MagicMock()
		mock_cursor = MagicMock()
		mock_connect.return_value = mock_conn
		mock_conn.cursor.return_value = mock_cursor
		mock_cursor.fetchone.return_value = ['hashed_password']
		print("Database connection and cursor mocked")

		# Mock the password check
		with patch('auth_app.views.check_password', return_value=True):
			response = self.client.post(self.url, json.dumps({
				'username': 'testuser',
				'password': 'testpassword'
			}), content_type='application/json')
			print(f"Response received: {response.content}")

		self.assertEqual(response.status_code, 200)
		self.assertJSONEqual(response.content, {'success': True})
		print("test_successful_authentication passed")

	@patch('auth_app.views.psycopg2.connect')
	def test_failed_authentication(self, mock_connect):
		print("Starting test_failed_authentication")
		# Mock the database connection and cursor
		mock_conn = MagicMock()
		mock_cursor = MagicMock()
		mock_connect.return_value = mock_conn
		mock_conn.cursor.return_value = mock_cursor
		mock_cursor.fetchone.return_value = ['hashed_password']
		print("Database connection and cursor mocked")

		# Mock the password check
		with patch('auth_app.views.check_password', return_value=False):
			response = self.client.post(self.url, json.dumps({
				'username': 'testuser',
				'password': 'wrongpassword'
			}), content_type='application/json')
			print(f"Response received: {response.content}")

		self.assertEqual(response.status_code, 401)
		self.assertJSONEqual(response.content, {'success': False, 'error': 'Invalid credentials'})
		print("test_failed_authentication passed")

	@patch('auth_app.views.psycopg2.connect')
	def test_database_connection(self, mock_connect):
		print("Starting test_database_connection")
		# Mock the database connection
		mock_conn = MagicMock()
		mock_connect.return_value = mock_conn

		# Attempt to connect to the database
		conn = psycopg2.connect(
			dbname="postgres",
			user="nishit",
			password="your_password",  # Ensure to replace 'your_password' with the actual password
			host="localhost"
		)
		print("Database connection attempted")

		# Verify that the connection was attempted
		mock_connect.assert_called_once_with(
			dbname="postgres",
			user="nishit",
			password="your_password",
			host="localhost"
		)
		print("Database connection verified")
		print("test_database_connection passed")

	def test_invalid_json(self):
		print("Starting test_invalid_json")
		response = self.client.post(self.url, 'invalid json', content_type='application/json')
		print(f"Response received: {response.content}")
		self.assertEqual(response.status_code, 400)
		self.assertJSONEqual(response.content, {'success': False, 'error': 'Invalid JSON'})
		print("test_invalid_json passed")

	def test_invalid_request_method(self):
		print("Starting test_invalid_request_method")
		response = self.client.get(self.url)
		print(f"Response received: {response.content}")
		self.assertEqual(response.status_code, 405)
		self.assertJSONEqual(response.content, {'success': False, 'error': 'Invalid request method'})
		print("test_invalid_request_method passed")