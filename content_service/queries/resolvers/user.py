from ariadne import ObjectType
from content_service.database import crud, SessionLocal

user_query = ObjectType("Query")

@user_query.field("user")
def resolve_user(_, info, id: int):
    db = SessionLocal()
    user = crud.get_user(db, user_id=id)
    db.close()
    if user:
        return user.__dict__
    return None
