from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.data.config import Settings

engine = create_engine(url=Settings.DATABASE_URL)
Session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
