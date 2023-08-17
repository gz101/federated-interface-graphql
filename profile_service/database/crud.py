from sqlalchemy.orm import Session
from .models import User, OrganizationMember

def get_user(db: Session, user_id: int):
    """Retrieve a User by their ID."""
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: dict):
    """Create a new User."""
    db_user = User(**user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_organization_member(db: Session, org_member_id: int):
    """Retrieve an OrganizationMember by their ID."""
    return db.query(OrganizationMember).filter(OrganizationMember.id == org_member_id).first()

def create_organization_member(db: Session, org_member: dict):
    """Create a new OrganizationMember."""
    db_org_member = OrganizationMember(**org_member)
    db.add(db_org_member)
    db.commit()
    db.refresh(db_org_member)
    return db_org_member
