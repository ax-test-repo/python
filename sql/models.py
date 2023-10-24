import os
import pytest
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from config import BASE_DIR

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String(100))
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(255))
    password = Column(String(100))
    phone = Column(String(100))

db_path = os.path.join(BASE_DIR, "sql", "pet_store_orm.db")
engine = create_engine(f"sqlite:///{db_path}")
Session = sessionmaker(bind=engine)

@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def valid_user():
    valid_user = User(
        id = 0,
        username = 'username_test',
        first_name = 'first_name_test',
        last_name = 'last_name_test',
        email = 'email@mail.ru',
        password = 'password',
        phone = '12345678'
    )
    return valid_user