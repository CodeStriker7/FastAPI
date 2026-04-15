from fastapi import APIRouter

router = APIRouter()

@router.get("/chek")
def chek_status():
    return {"status": "Good luck"}
