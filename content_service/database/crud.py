from sqlalchemy.orm import Session
from .models import User

def get_user(db: Session, user_id: int):
    """Retrieve a User by their ID."""
    return db.query(User).filter(User.contentId == user_id).first()

def create_user(db: Session, user: dict):
    """Create a new User."""
    db_user = User(**user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
