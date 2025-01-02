from typing import Optional
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from enum import Enum as PyEnum
from pydantic import BaseModel, Field

Base = declarative_base()

class State(str, PyEnum):
    PENDENTE = "PENDENTE"
    EM_ANDAMENTO = "EM_ANDAMENTO"
    CONCLUIDA = "CONCLUIDA"
    
class TaskCreate(BaseModel):
    title: str = Field(..., description="Título da tarefa", max_length=255)
    description: Optional[str] = Field(None, description="Descrição opcional da tarefa")
    state: State = Field(..., description="Estado atual da tarefa")

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, description="Título da tarefa", max_length=255)
    description: Optional[str] = Field(None, description="Descrição opcional da tarefa")
    state: Optional[State] = Field(None, description="Estado atual da tarefa")

class TaskResponse(BaseModel):
    id: Optional[int] = Field(None, description="Id tarefa")
    title: Optional[str] = Field(None, description="Título da tarefa", max_length=255)
    description: Optional[str] = Field(None, description="Descrição opcional da tarefa")
    state: Optional[State] = Field(None, description="Estado atual da tarefa")
    created_at: Optional[datetime] = Field(None, description="Estado atual da tarefa")
    updated_at: Optional[datetime] = Field(None, description="Estado atual da tarefa")

class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(String, nullable=True)
    state = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.now)
    updated_at = Column(TIMESTAMP, default=datetime.now, onupdate=datetime.now)
