from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, index=True)
    title = Column(String)
    completed = Column(Boolean, default=False)