from sqlalchemy.orm import declarative_base
from sqlalchemy import VARCHAR, Integer, Column

Base = declarative_base()

class Users(Base):
    __tablename__ ='usersc'
    id = Column(VARCHAR(8),primary_key=True)
    first_name = Column(VARCHAR(50))
    last_name = Column(VARCHAR(50))
    age = Column(Integer)
    email = Column(VARCHAR(50))


