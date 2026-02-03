"""
Test script to isolate the auth issue
"""
import sys
import os

# Add the parent directory to Python path so 'backend' package can be found
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from config.database import SessionLocal
from app.models.user import User
from sqlalchemy.orm import sessionmaker
from config.database import engine

def test_user_query():
    try:
        print("Testing user query without relationships...")

        # Create a session using the same method as auth.py
        db = SessionLocal()

        # Try a simple query without loading relationships
        user = db.query(User).first()
        print(f"Simple query worked, found user: {user}")

        # Try counting users
        user_count = db.query(User).count()
        print(f"User count: {user_count}")

        db.close()
        print("Simple queries work!")
        return True

    except Exception as e:
        print(f"Error in simple user query: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_user_creation():
    try:
        print("\nTesting user creation...")

        db = SessionLocal()

        # Try creating a user similar to auth.py
        from uuid import uuid4
        from auth.utils import get_password_hash

        new_user = User(
            id=str(uuid4()),
            email="test@example.com",
            hashed_password=get_password_hash("password123"),
            is_active=True
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        print(f"User created successfully with ID: {new_user.id}")
        print(f"Has created_at: {hasattr(new_user, 'created_at')}")

        # Clean up
        db.delete(new_user)
        db.commit()
        db.close()

        print("User creation works!")
        return True

    except Exception as e:
        print(f"Error in user creation: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_user_query()
    test_user_creation()