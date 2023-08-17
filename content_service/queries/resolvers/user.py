from ariadne import ObjectType
from content_service.database.crud import get_user
from content_service.database.config import SessionLocal

user_query = ObjectType("Query")

@user_query.field("user")
def resolve_user(_, info, id: int):
    db = SessionLocal()
    user = get_user(db, user_id=id)
    db.close()
    if user:
        return user.__dict__
    return None
