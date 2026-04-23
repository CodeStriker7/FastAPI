from fastapi import APIRouter
import psutil
from app.schemas.disk import DiskResponse

router = APIRouter()

@router.get("/disk", response_model=DiskResponse)
async def disk_status():
    # Funksiya ichidagi barcha qatorlar bir xil darajada surilishi kerak
    usage = psutil.disk_usage('/')
    return {
        "total_gb": round(usage.total / (2**30), 2),
        "used_gb": round(usage.used / (2**30), 2),
        "free_gb": round(usage.free / (2**30), 2),
        "percent": usage.percent
    }