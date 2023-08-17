from profile_service.database.config import Base, engine, SessionLocal
from profile_service.database import crud
from profile_service.database.models import User, OrganizationMember

def init_db():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    # Seeding User
    user = crud.get_user(db, user_id=1)
    if not user:
        crud.create_user(db, user={"id": 1, "email": "user1@gmail.com", "individualId": 12345})

    # Seeding OrganizationMember
    org_member = crud.get_organization_member(db, org_member_id=1)
    if not org_member:
        crud.create_organization_member(db, org_member={"id": 1, "email": "member1@gmail.com", "organizationId": 54})

    db.close()

if __name__ == "__main__":
    init_db()
