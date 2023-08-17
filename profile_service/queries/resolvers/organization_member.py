from ariadne import ObjectType
from sqlalchemy.orm import Session
from profile_service.database.crud import get_organization_member
from profile_service.database.models import OrganizationMember as OrganizationMemberModel
from profile_service.database import DATABASE_URL, SessionLocal
from profile_service.queries.resolvers.query import query

def resolve_organization_member_query(obj, info, id: int):
    db = SessionLocal()
    organization_member = get_organization_member(db, id)
    db.close()
    if organization_member:
        return organization_member.__dict__
    return None
