from fastapi import APIRouter
from app.api.v1.endpoints import status
from app.api.v1.endpoints import disk

api_router = APIRouter()

api_router.include_router(
    status.router, 
    prefix="/status", 
    tags=["Health Check"] 
)

api_router.include_router(
    disk.router, 
    prefix="/disk", 
    tags=["Disk Info"] 
)