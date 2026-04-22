from pydantic import BaseModel

class StatusResponse(BaseModel):
    status: str
    service: str
    timestamp: str
    os: str
    version: str