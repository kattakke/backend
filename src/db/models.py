from sqlalchemy import create_engine, Column, DateTime, String, UUID, text, VARCHAR, CHAR, TIMESTAMP, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
global session
class DBUser(Base):
    __tablename__ = 'users'
    userId = Column(UUID, primary_key=True,
                       server_default=text('gen_random_uuid()'))
    name = Column(VARCHAR, nullable=False)
    password = Column(VARCHAR, nullable=False)
    jwt_secret = Column(VARCHAR, nullable=False)
    shelf = Column(UUID, nullable=False, server_default=text('gen_random_uuid()'))
    createdAt = Column(TIMESTAMP, nullable=False, server_default=text(
        'CURRENT_TIMESTAMP'))
    updatedAt = Column(TIMESTAMP, nullable=False, server_default=text(
        'CURRENT_TIMESTAMP'))
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
class DBShelf(Base):
    __tablename__ = 'shelves'
    id = Column(UUID, primary_key=True,
                       server_default=text('gen_random_uuid()'))
    shelfId = Column(UUID)
    book = Column(UUID, ForeignKey("books.bookId"))
    createdAt = Column(TIMESTAMP, nullable=False, server_default=text(
        'CURRENT_TIMESTAMP'))
    updatedAt = Column(TIMESTAMP, nullable=False, server_default=text(
        'CURRENT_TIMESTAMP'))
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class DBBook(Base):
    __tablename__ = 'books'
    bookId = Column(UUID, primary_key=True, 
                       server_default=text('gen_random_uuid()'))
    isbn = Column(VARCHAR, nullable=True)
    title = Column(VARCHAR, nullable=False)
    author = Column(VARCHAR, nullable=True)
    publisher = Column(VARCHAR, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text(
        'CURRENT_TIMESTAMP'))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text(
        'CURRENT_TIMESTAMP'))
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

def init_db(uri):
    global session
    engine = create_engine(uri)
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False,
                                             bind=engine))
    Base.query = db_session.query_property()
    Base.metadata.create_all(bind=engine)
    session = db_session
    return db_session

def Session():
    global session
    if session is None:
        raise NotImplementedError
    return session
