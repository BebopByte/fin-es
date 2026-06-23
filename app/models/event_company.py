from sqlalchemy import Table, Column, ForeignKey
from app.db.base import Base

event_company = Table(
    "event_company",
    Base.metadata,

    Column("event_id", ForeignKey("events.id"), primary_key=True),
    Column("company_id", ForeignKey("companies.id"), primary_key=True),
)