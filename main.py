
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from additional import create_tables, Publisher, Book


DSN = "postgresql://postgres:пароль@localhost:5432/bookshops"
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.close()
