from fastapi import APIRouter

router = APIRouter()

@router.get("/chek")
def chek_status():
    return {"status": "Good luck bro"}
# get /test http://127.0.0.1:8000/api/v1/status/test
@router.get("/test")
def again():
    return {"status": "again try"}
