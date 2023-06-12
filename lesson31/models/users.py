from sqlalchemy.orm import declarative_base
from sqlalchemy import VARCHAR, Integer, Column

Base = declarative_base()

class Users(Base):
    __tablename__ ='usersc'
    id = Column(VARCHAR(8),primary_key=True)
    first_name = Column(VARCHAR(50))
    age = Column(Integer)
    email = Column(VARCHAR(50))

    def __str__(self):
        return f" id = {self.id}, first_name = {self.first_name}, age = {self.age}, email = {self.email}"


