from fastapi import APIRouter, Depends, HTTPException
from app.dependencies.bloomberg import bbconnect
from app.models import BDHRequest
from blp import blp
import pandas as pd
import json


router = APIRouter()


@router.post("/", summary="Download time-series data.", operation_id="bdh")
async def get_bdh(request: BDHRequest, bquery: blp.BlpQuery = Depends(bbconnect)):
    try:
        data = bquery.bdh(
            request.tickers,
            request.fields,
            start_date=request.start_date,
            end_date=request.end_date,
            options=request.options,
            overrides=request.overrides,
        )

        result = json.loads(data.to_json(orient="records", date_format="iso"))
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
