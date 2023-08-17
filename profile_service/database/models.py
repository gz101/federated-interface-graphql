from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    email = Column(String(100))
    individualId = Column(Integer)

class OrganizationMember(Base):
    __tablename__ = 'OrganizationMembers'
    id = Column(Integer, Sequence('org_member_id_seq'), primary_key=True)
    email = Column(String(100))
    organizationId = Column(String(50))
