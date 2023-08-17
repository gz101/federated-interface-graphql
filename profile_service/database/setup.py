from content_service.database.config import Base, engine
from profile_service.database.models import User, OrganizationMember

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
