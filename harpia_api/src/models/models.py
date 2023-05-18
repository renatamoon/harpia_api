# THIRD PART IMPORTS
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    description = Column(String)


class Claim(Base):
    __tablename__ = 'claims'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    active = Column(Boolean, default=True)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    role_id = Column(Integer, ForeignKey('roles.id'))
    created_at = Column(Date)
    updated_at = Column(Date)
    role = relationship("Role", backref="users")


class UserClaim(Base):
    __tablename__ = 'user_claims'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    claim_id = Column(Integer, ForeignKey('claims.id'), primary_key=True)
