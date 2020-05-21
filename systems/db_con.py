from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from common import cred
from common import pyd_models, db_models

import os
import logging
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

# PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql://{}:{}@{}/{}".format(
    cred.postgres_user, cred.postgres_pw, cred.postgres_uri, cred.postgres_db
)
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
