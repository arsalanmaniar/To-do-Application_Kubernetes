"""
Test auth functions directly to see the error
"""
import sys
import os

# Add the parent directory to Python path so 'backend' package can be found
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from config.database import SessionLocal
from schemas.user import UserCreate
from api.v1.auth import register
import traceback

try:
    print("Testing register function directly...")

    # Create a test user data
    user_data = UserCreate(email="test@example.com", password="testpassword123")

    # Create a database session
    db = SessionLocal()

    # Call the register function directly
    result = register(user_data, db)

    print(f"Register successful: {result}")
    db.close()

except Exception as e:
    print(f"Error in register function: {e}")
    print("Full traceback:")
    traceback.print_exc()