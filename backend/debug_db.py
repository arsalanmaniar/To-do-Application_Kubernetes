"""
Debug script to test database operations directly
"""
import sys
import os

# Add the parent directory to Python path so 'backend' package can be found
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from config.database import get_db, engine
from app.models.user import User
from sqlmodel import Session, select
import traceback

try:
    print("Testing direct SQLModel operations...")

    # Create a session
    db = Session(engine)

    # Try to query users (similar to what auth does)
    statement = select(User)
    users = db.exec(statement).all()
    print(f"Found {len(users)} users in database")

    # Try to create a test user directly with SQLModel
    from uuid import uuid4
    from app.models.user import User as UserModel
    from auth.utils import get_password_hash

    new_user = UserModel(
        id=str(uuid4()),
        email="test@example.com",
        hashed_password=get_password_hash("password123"),
        is_active=True
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    print(f"Created user with ID: {new_user.id}")
    print(f"User has created_at: {hasattr(new_user, 'created_at')}")
    if hasattr(new_user, 'created_at'):
        print(f"Created at: {new_user.created_at}")

    db.delete(new_user)
    db.commit()
    print("Test user deleted successfully")

    db.close()
    print("Direct SQLModel operations work correctly!")

except Exception as e:
    print(f"Error in direct SQLModel operations: {e}")
    traceback.print_exc()