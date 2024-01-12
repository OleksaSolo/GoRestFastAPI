from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:567234@localhost:5432/postgres"
# SQLALCHEMY_DATABASE_URL = "postgres://koyeb-adm:XP7mswbKhYU8@ep-broad-dew-69547104.eu-central-1.pg.koyeb.app/koyebdb"
#SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg2://postgres:567234@localhost:5432/postgres"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
