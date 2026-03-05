
from sqlalchemy import Column, Integer, String
from dataconnect import Base

class User(Base):
    __tablename__ = "user"
    
    user_id = Column(Integer, primary_key=True, nullable=True)
    username = Column(String(50), index=True, nullable=True)
    email = Column(String(100), unique=True, index=True, nullable=True)
    password_hash = Column(String(100), nullable=True)
    user_type = Column(String(20), nullable=True)  # 'applicant' 或 'employer'
    avatar_url = Column(String(200), nullable=True)

class Job(Base):
    __tablename__ = "job"
    
    job_id = Column(Integer, primary_key=True, nullable=True)
    job_title = Column(String(100), index=True, nullable=True)
    job_description = Column(String(500), nullable=True)
    company = Column(String(100), nullable=True)
    company_size = Column(String(50), nullable=True)
    minor_category_id = Column(Integer, nullable=True)
    job_location = Column(String(100), nullable=True)
    salary = Column(String(50), nullable=True)
    education_requirement = Column(String(100), nullable=True)
    job_nature = Column(String(50), nullable=True)  # 全职、兼职等
    