from pydantic import BaseModel

class GieBaseRequest(BaseModel):
    target: str
    start_date: str
    end_date: str


