from pydantic import BaseModel

class BDIPRequest(BaseModel):
    ticker: str
    event_type: str = "TRADE"
    interval: int = 1
    start_datetime: str
    end_datetime: str


