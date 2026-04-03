from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import SessionLocal
from models import Result, Candidate, Party, District, Election
from schemas import DistrictResults

router = APIRouter(prefix="/districts")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{district_id}/results", response_model=DistrictResults)
def get_district_results(
    district_id: int,
    election_year: int,
    db: Session = Depends(get_db)
):
    election = db.query(Election).filter(Election.year == election_year).one()
    district = (
        db.query(District.fedname)
        .filter(District.id == district_id)
        .one()
    )

    rows = (
        db.query(Result, Candidate, Party)
        .join(Candidate, Result.candidate_id == Candidate.id)
        .join(Party, Result.party_id == Party.id)
        .filter(
            Result.district_id == district_id,
            Result.election_id == election.id
        )
        .order_by(Result.votes.desc())
        .all()
    )


    return {
        "district": district.fedname,
        "election_year": election.year,
        "results": [
            {
                "candidate": c.name,
                "party": p.name,
                "occupation": c.occupation or "",
                "votes": r.votes,
                "result": r.result
            }
            for r, c, p in rows
        ]
    }


@router.get("/{district_id}/geojson")
def get_district_geojson(district_id: int, db: Session = Depends(get_db)):
    query = text("""
        SELECT jsonb_build_object(
            'type', 'Feature',
            'geometry', ST_AsGeoJSON(geom)::jsonb,
            'properties', jsonb_build_object(
                'id', id,
                'fedname', fedname
            )
        )
        FROM districts
        WHERE id = :district_id
    """)

    result = db.execute(query, {"district_id": district_id}).fetchone()

    if not result:
        return {"error": "District not found"}

    return result[0]


@router.get("/geojson")
def get_all_districts(election_year: int, db: Session = Depends(get_db)):

    query = text("""
    WITH election_boundary AS (
        SELECT id, boundary_version_id
        FROM elections
        WHERE year = :election_year
    ),

    winners AS (
        SELECT DISTINCT ON (r.district_id)
            r.district_id,
            p.name AS party_name
        FROM results r
        JOIN election_boundary e ON r.election_id = e.id
        JOIN parties p ON r.party_id = p.id
        ORDER BY r.district_id, r.votes DESC
    )

    SELECT jsonb_build_object(
        'type', 'FeatureCollection',
        'features', COALESCE(
            jsonb_agg(
                jsonb_build_object(
                    'type','Feature',
                    'geometry', ST_AsGeoJSON(d.geom)::jsonb,
                    'properties', jsonb_build_object(
                        'id', d.id,
                        'fedname', d.fedname,
                        'party', w.party_name
                    )
                )
            ),
            '[]'::jsonb
        )
    )
    FROM districts d
    JOIN election_boundary eb
        ON d.election_id = eb.id
    LEFT JOIN winners w
        ON d.id = w.district_id;
    """)

    result = db.execute(query, {"election_year": election_year}).fetchone()

    return result[0]



@router.get("/{election_year}/{candidate_id}/geojson")
def get_district_from_candidate(election_year: int, candidate_id: int, db: Session = Depends(get_db)):

    election = db.query(Election).filter(Election.year == election_year).one()

    query = text("""
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
        SELECT 
            districts.id,
            districts.fedname,
            districts.geom
        FROM districts
        JOIN results
        ON results.district_id = districts.id
        WHERE candidate_id = :candidate_id
        AND districts.election_id = :election_id
        ) sub;
""")

    result = db.execute(query, {'candidate_id': candidate_id, 'election_id': election.id}).fetchone()
    return result[0]
