from content_service.database.config import Base, engine, SessionLocal
from content_service.database import models, crud

def init_db():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    # Seeding User
    user = crud.get_user(db, user_id=1)
    if not user:
        crud.create_user(db, user={"id": 1, "contentMessage": "hello"})

    db.close()

if __name__ == "__main__":
    init_db()
