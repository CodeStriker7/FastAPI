from fastapi import APIRouter
from app.schemas.status import StatusResponse
import platform
from datetime import datetime 
import time

router = APIRouter()

@router.get("/chek", response_model=StatusResponse)
def chek_status():
    formatted_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {
    "status": "Great",
    "service": "monitoring",
    "timestamp": formatted_time,
    "os": platform.system(),
    "version": "1.0.0"
    }
  