from pydantic import BaseModel, field_validator
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime

class BloombergBaseRequest(BaseModel):
    tickers: List[str]
    fields: List[str]
    options: Optional[Dict[str, Any]] = {}
    overrides: Optional[List[Tuple[str, str]]] = []


class BDHRequest(BloombergBaseRequest):
    start_date: Optional[str] = None
    end_date: Optional[str] = None


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


class BDPRequest(BloombergBaseRequest):
    pass


class BDSRequest(BloombergBaseRequest):
    pass
