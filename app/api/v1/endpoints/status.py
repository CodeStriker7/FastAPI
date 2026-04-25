from fastapi import APIRouter
from app.schemas.status import StatusResponse
import platform
from datetime import datetime 
import time
import psutil

router = APIRouter()

@router.get("/check", response_model=StatusResponse)
async def chek_status():
    formatted_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {
    "status": "Great",
    "service": "monitoring",
    "timestamp": formatted_time,
    "os": platform.system(),
    "version": "1.0.0",
    "cpu_usage_percent": psutil.cpu_percent(interval=1), # Real CPU 
    "ram_usage_percent": psutil.virtual_memory().percent # Real RAM 
    }
