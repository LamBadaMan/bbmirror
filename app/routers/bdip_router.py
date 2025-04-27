from fastapi import APIRouter, Depends, HTTPException
from app.dependencies.bloomberg import bbconnect
from app.models import BDIPRequest
from blp import blp
import pandas as pd
import json


router = APIRouter()


@router.post("/", summary="Download intraday bars.", operation_id="bdip")
async def get_bdip(request: BDIPRequest, bquery: blp.BlpQuery = Depends(bbconnect)):
    try:
        data = bquery.bdib(
            request.ticker,
            request.event_type,
            interval=request.interval,
            start_datetime=request.start_datetime,
            end_datetime=request.end_datetime,
        )

        result = json.loads(data.to_json(orient="records", date_format="iso"))
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
