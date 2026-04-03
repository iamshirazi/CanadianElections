from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from geoalchemy2 import Geometry

class Election(Base):
    __tablename__ = "elections"
    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    boundary_version_id = Column(Integer)

class DistrictAlias(Base):
    __tablename__ = "district_aliases"
    id = Column(Integer, primary_key=True)
    alias_name = Column(Integer)
    district_id = Column(Integer)

class District(Base):
    __tablename__ = "districts"
    id = Column(Integer, primary_key=True, index=True)
    boundary_version_id = Column(Integer)
    fedname = Column(String)
    shape_area = Column(Integer)
    geom = Column(Geometry("MULTIPOLYGON", srid=4326))
    election_id = Column(Integer, ForeignKey("elections.id"), nullable=True)

class Party(Base):
    __tablename__ = "parties"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Candidate(Base):
    __tablename__ = "candidates"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    occupation = Column(String, nullable=True)
    election_id = Column(Integer, ForeignKey("elections.id"))
    district_id = Column(Integer, ForeignKey("districts.id"))

class Result(Base):
    __tablename__ = "results"
    id = Column(Integer, primary_key=True)
    election_id = Column(Integer, ForeignKey("elections.id"))
    district_id = Column(Integer, ForeignKey("districts.id"))
    candidate_id = Column(Integer, ForeignKey("candidates.id"))
    party_id = Column(Integer, ForeignKey("parties.id"))
    votes = Column(Integer)
    result = Column(String)
