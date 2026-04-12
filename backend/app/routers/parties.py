from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Result, Party, Election
from schemas import Parties

router = APIRouter(prefix="/parties")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=Parties)
async def get_parties(
    election_year: int,
    db: Session = Depends(get_db)
):
    election = db.query(Election).filter(Election.year == election_year).one()

    rows = (
        db.query(Party)
        .join(Result, Result.party_id == Party.id)
        .filter(
            Result.election_id == election.id,
            Result.result.contains("Elected")
        )
        .distinct()
        .order_by(Party.name.asc())
        .all()
    )

    return {
        "parties": [p.name for p in rows]
    }