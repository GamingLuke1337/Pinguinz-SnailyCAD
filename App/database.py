from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_CONFIG

DATABASE_URL = "mysql+pymysql://username:password@localhost:3306/database_name"

engine = create_engine(DATABASE_URL, connect_args={"auth_plugin": "mysql_native_password"})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency für DB-Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
