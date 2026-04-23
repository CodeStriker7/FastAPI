from pydantic import BaseModel

class StatusResponse(BaseModel):
    status: str
    service: str
    timestamp: str
    os: str
    version: str
    cpu_usage_percent: float
    ram_usage_percent: float
    disk_free_gb: float