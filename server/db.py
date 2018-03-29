from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()
class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  password = Column(String)
  salt = Column(String)

  def __repr__(self):
    return "User %d %s" % (self.id, self.name)


Base.metadata.create_all(engine)
