from sqlalchemy import create_engine
from profile_service.database.models import Base, User, OrganizationMember
from .config import DATABASE_URL

engine = create_engine(DATABASE_URL)

# Create tables in the database
Base.metadata.create_all(bind=engine)
