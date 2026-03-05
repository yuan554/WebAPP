
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# MySQL数据库连接配置 - 请根据实际情况修改
DATABASE_URL = "mysql+pymysql://root:y3462qwe@localhost:3306/zhaopin_db"

# 创建引擎和会话
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """
    获取数据库会话
    """
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()