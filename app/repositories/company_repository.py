from sqlalchemy.orm import Session
from app.models.company import Company

class CompanyRepository:

    def __init__(self, db: Session):
        self.db = db

    def add_company(self, company: Company) -> Company:
        self.db.add(company)
        self.db.commit()
        self.db.refresh(company)
        return company
    
    def get_by_ticker(self, ticker: str) -> Company | None:
        return(
            self.db.query(Company)
            .filter(Company.ticker == ticker)
            .first()
        )
    
    def get_all(self) -> list[Company]:
        return self.db.query(Company).all()