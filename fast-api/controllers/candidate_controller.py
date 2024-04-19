from fastapi import APIRouter, HTTPException
from typing import List
from models.candidate import Candidate
from database2 import Database

router = APIRouter()
db = Database()

@router.get("/candidates", response_model=List[Candidate])
async def get_candidates():
    try:
        candidates = db.get_all_candidates()
        return candidates
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/candidates/{candidate_id}", response_model=Candidate)
async def get_candidate(candidate_id: int):
    try:
        candidate = db.get_candidate_by_id(candidate_id)
        if candidate:
            return candidate
        else:
            raise HTTPException(status_code=404, detail="Candidate not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


