from pydantic import BaseModel

class DiskResponse(BaseModel):
    total_gb: float    
    used_gb: float     
    free_gb: float     
    percent: float     