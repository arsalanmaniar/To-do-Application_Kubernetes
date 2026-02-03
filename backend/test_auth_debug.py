"""
Debug script to test the auth endpoints and see the actual error
"""
import requests
import json

# Test the register endpoint
try:
    response = requests.post(
        'http://localhost:8000/auth/register',
        headers={'Content-Type': 'application/json'},
        json={
            'email': 'testuser@example.com',
            'password': 'testpassword123',
            'name': 'Test User'
        },
        timeout=10
    )
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")

# Also test the login endpoint
try:
    response = requests.post(
        'http://localhost:8000/auth/login',
        headers={'Content-Type': 'application/json'},
        json={
            'email': 'testuser@example.com',
            'password': 'testpassword123'
        },
        timeout=10
    )
    print(f"Login Status Code: {response.status_code}")
    print(f"Login Response: {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Login request failed: {e}")