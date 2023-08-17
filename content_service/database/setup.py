from content_service.database.config import Base, engine
from content_service.database.models import User

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
