from pydantic import BaseModel
from typing import Optional, List
from model.client import Client


class CreateClientSchema(BaseModel):
    """ Schema criação de um cliente
    """
    name: str = "Cliente teste"
    email: str = "teste@gmail.com"
    phone: str = "1234567890"
    document: Optional[str] = None

 