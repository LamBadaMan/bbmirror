from pydantic import BaseModel
from typing import List, Dict, Any, Optional, Tuple


class BloombergBaseRequest(BaseModel):
    tickers: List[str]
    fields: List[str]
    options: Optional[Dict[str, Any]] = {}
    overrides: Optional[List[Tuple[str, str]]] = []
