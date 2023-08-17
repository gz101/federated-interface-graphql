from sqlalchemy.orm import Session
from .models import User, OrganizationMember

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_organization_member(db: Session, org_member_id: int):
    return db.query(OrganizationMember).filter(OrganizationMember.id == org_member_id).first()
