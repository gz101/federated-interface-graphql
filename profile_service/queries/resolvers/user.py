from ariadne import ObjectType
from sqlalchemy.orm import Session
from profile_service.database.crud import get_user
from profile_service.database.models import User as UserModel
from profile_service.database import DATABASE_URL, SessionLocal
from profile_service.queries.resolvers.query import query

@query.field("user")
def resolve_user_query(obj, info, id: int):
    db = SessionLocal()
    user = get_user(db, id)
    db.close()
    if user:
        return user.__dict__
    return None
