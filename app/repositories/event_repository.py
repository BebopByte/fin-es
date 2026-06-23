from sqlalchemy.orm import Session
from app.models.event import Event
from app.models.event_company import event_company

class EventRepository:

    def __init__(self, db: Session):
        self.db = db

    def add_event(self, event: Event, company_ids: list[int]) -> Event:
        self.db.add(event)
        self.db.flush()

        for cid in company_ids:
            self.db.execute(
                event_company.insert().values(
                    event_id=event.id,
                    company_id=cid,
                )
            )
        self.db.commit()
        self.db.refresh(event)
        return event
    
    def get_all(self):
        return self.db.query(Event).all()