from pydantic import BaseModel
from typing import Optional, List
from app.enums.event_status import EventStatus

class EventCreate(BaseModel):
    event_type: str
    title: str
    description: Optional[str] = None
    company_ids: List[int]

class EventResponse(BaseModel):
    id: int
    event_type: str
    title: str
    description: Optional[str]
    status: EventStatus

    class Config:
        from_attributes = True