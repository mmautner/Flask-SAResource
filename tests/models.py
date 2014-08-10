
from sqlalchemy import *
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
 
def sqlalchemy_session(db_uri):
    engine = create_engine(db_uri, convert_unicode=True)
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))
    return db_session

Base = declarative_base()
 
class Todo(Base):
    __tablename__ = 'todos'
 
    id = Column(Integer, primary_key=True)
    task = Column(String(255))
