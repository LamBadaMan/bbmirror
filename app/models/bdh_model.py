from app.models.base import BloombergBaseRequest
from typing import List, Dict, Any, Optional, Tuple


class BDHRequest(BloombergBaseRequest):
    start_date: Optional[str] = None
    end_date: Optional[str] = None
