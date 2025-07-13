from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from config import MYSQL_URL, POSTGRES_URL


    
def get_mysql_engine():
    engine = create_engine(MYSQL_URL)
    try:
        with engine.connect() as connection:
            print("MySQL: соединение установлено успешно")
        return engine
    except SQLAlchemyError as e:
        print(f"Ошибка подключения к MySQL: {e}")
        return None

def get_postgres_engine():
    engine = create_engine(POSTGRES_URL)
    try:
        with engine.connect() as connection:
            print("PostgreSQL: соединение установлено успешно")
        return engine
    except SQLAlchemyError as e:
        print(f"Ошибка подключения к PostgreSQL: {e}")
        return None

