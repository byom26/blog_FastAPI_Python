from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DB_URL = 'sqlite:///./blog.db'

engine = create_engine(SQLALCHEMY_DB_URL, connect_args={'check_same_thread':False})

sessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()