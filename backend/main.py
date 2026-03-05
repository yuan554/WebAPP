from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # 添加CORS中间件导入
from dataconnect import engine, get_db
from data import User, Job
import uvicorn
from typing import List

app = FastAPI()

# 添加CORS中间件，允许前端页面访问API
# 对于开发阶段，允许所有源，但在生产环境中应限制为具体域名
# 特别为本地HTML文件(file://协议)添加支持
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 开发期间允许所有源，生产环境应限制为具体域名
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有HTTP方法
    allow_headers=["*"],  # 允许所有请求头
    # 允许浏览器发送cookies和其他认证信息
    allow_origin_regex=None,
    # 在响应头中暴露某些headers
    expose_headers=["Access-Control-Allow-Origin"]
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/test-db")
def test_db_connection():
    try:
        # 尝试连接数据库
        connection = engine.connect()
        connection.close()
        return {"message": "数据库连接成功!"}
    except Exception as e:
        return {"error": f"数据库连接失败: {str(e)}"}


@app.get("/users")
def get_users(skip: int = 0, limit: int = 100):
    """
    获取用户列表
    """
    db = get_db()
    try:
        users = db.query(User).offset(skip).limit(limit).all()
        return users
    finally:
        db.close()


@app.get("/users/{user_id}")
def get_user(user_id: int):
    """
    根据ID获取特定用户
    """
    db = get_db()
    try:
        user = db.query(User).filter(User.user_id == user_id).first()
        if user is None:
            return {"error": "用户不存在"}
        return user
    finally:
        db.close()


@app.get("/jobs")
def get_jobs(skip: int = 0, limit: int = 100):
    """
    获取职位列表
    """
    db = get_db()
    try:
        jobs = db.query(Job).offset(skip).limit(limit).all()
        return jobs
    finally:
        db.close()


@app.get("/jobs/{job_id}")
def get_job(job_id: int):
    """
    根据ID获取特定职位
    """
    db = get_db()
    try:
        job = db.query(Job).filter(Job.job_id == job_id).first()
        if job is None:
            return {"error": "职位不存在"}
        return job
    finally:
        db.close()


@app.get("/jobs/search/description")
def search_jobs_by_description(description: str):
    """
    根据职位描述搜索职位
    """
    db = get_db()
    try:
        # 使用模糊匹配查询职位描述
        jobs = db.query(Job).filter(Job.job_description.like(f"%{description}%")).all()
        return jobs
    finally:
        db.close()


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)