from fastapi import APIRouter, HTTPException, status


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/token")
async def get_bearer_token():
    pass
