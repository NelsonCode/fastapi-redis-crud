from pydantic import BaseModel, Field
from uuid import uuid4
from datetime import datetime


def generate_uuid():
    return str(uuid4())


def generate_date():
    return str(datetime.now())


class Product(BaseModel):
    id: str = Field(default_factory=generate_uuid)
    name: str
    price: float
    date: str = Field(default_factory=generate_date)
