from enum import Enum
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field

class State(str, Enum):
    PENDENTE = "pendente"
    EM_ANDAMENTO = "em andamento"
    CONCLUIDA = "concluída"

class Task(BaseModel):
    id: Optional[int] = Field(default=None, description="ID autoincrementado da tarefa")
    title: str = Field(..., description="Título da tarefa", max_length=255)
    description: Optional[str] = Field(None, description="Descrição opcional da tarefa")
    state: State = Field(..., description="Estado atual da tarefa")
    created_at: datetime = Field(..., description="Data de criação da tarefa")
    updated_at: datetime = Field(..., description="Data de última atualização")

    def atualizar_estado(self, new_state: State):
        self.state = new_state
        self.updated_at = datetime.now()