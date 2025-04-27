from pydantic import BaseModel, field_validator
from datetime import datetime

class BDIPRequest(BaseModel):
    ticker: str
    event_type: str = "TRADE"
    interval: int = 1
    start_datetime: str
    end_datetime: str

    @field_validator('start_datetime', 'end_datetime', mode='before')
    @classmethod
    def parse_date(cls, v):
        if isinstance(v, str) and len(v) == 8:
            dt = datetime.strptime(v, "%Y%m%d")
            return dt.strftime("%Y-%m-%d")
        return v

