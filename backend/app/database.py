import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = None

for i in range(10):
    try:
        engine = create_engine(DATABASE_URL)
        engine.connect()
        print("Database connected!")
        break
    except OperationalError:
        print("Database not ready, retrying...")
        time.sleep(2)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()