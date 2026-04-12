from pydantic import BaseModel

class CandidateResult(BaseModel):
    candidate: str
    party: str
    occupation: str
    votes: int
    result: str

class DistrictResults(BaseModel):
    district: str
    election_year: int
    results: list[CandidateResult]

class SearchItem(BaseModel):
    id: int
    name: str
    type: str

class Parties(BaseModel):
    parties: list[str]
