from fastapi import APIRouter
from endpoints import forward

router = APIRouter()

router.include_router(forward.router, tags=["Forward"])