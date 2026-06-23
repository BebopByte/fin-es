from pydantic import BaseModel
from typing import Optional

class CompanyCreate(BaseModel):
    ticker: str
    name: str
    industry: Optional[str] = None

class CompanyResponse(BaseModel):
    id: int
    ticker: str
    name: str
    industry: Optional[str]

    class Config:
        from_attributes: True