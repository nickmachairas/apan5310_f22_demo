from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine("postgresql://postgres:123@localhost/etl_demo")
Base = declarative_base()
