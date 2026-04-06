from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import SessionLocal
from models import Candidate, Election

router = APIRouter(prefix="/search")

def get_db():
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()

@router.get("")
async def search(
    query: str = Query(..., min_length=1, max_length=30),
    election_year: int = Query(...), 
    db: Session = Depends(get_db)
):

    election = db.query(Election).filter(Election.year == election_year).one()

    candidates = (
        db.query(Candidate)
        .join(Election)
        .filter(
            Election.year == election_year,
            Candidate.name.like(f"%{query}%")
        )
        .limit(5)
        .all()
    )


    district_string = f"%{query}%"

    district_query = text("""
    SELECT jsonb_build_object(
        'type', 'FeatureCollection',
        'features', COALESCE(jsonb_agg(
            jsonb_build_object(
                'type', 'Feature',
                'geometry', ST_AsGeoJSON(geom)::jsonb,
                'properties', jsonb_build_object(
                    'id', id,
                    'fedname', fedname
                )
            )
        ), '[]'::jsonb)
    )
    FROM (
        SELECT districts.id, districts.fedname, districts.geom
        FROM districts
        JOIN elections 
            ON districts.election_id = elections.id 
        WHERE fedname ILIKE :district_string
            AND elections.id = :election_id 
        LIMIT 5
    ) sub;
""")


    districts = db.execute(district_query, {"district_string": district_string, "election_id": election.id}).all()

    return {
        "candidates": candidates,
        "districts": districts[0][0]
    }
