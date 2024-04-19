from sqlalchemy import Column, Integer, String
from database import Base

class TeamMember(Base):
    __tablename__ = 'team_members'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    email = Column(String, nullable=False)
