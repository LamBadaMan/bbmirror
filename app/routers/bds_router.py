from fastapi import APIRouter, Depends, HTTPException
from app.dependencies.bloomberg import bbconnect
from app.models import BDSRequest
from blp import blp
import pandas as pd
import json


router = APIRouter()


@router.post("/", summary="Download bulk data.", operation_id="bds")
async def get_bds(request: BDSRequest, bquery: blp.BlpQuery = Depends(bbconnect)):
    try:
        data = bquery.bds(request.tickers, request.fields, options=request.options, overrides=request.overrides)

        result = json.loads(data.to_json(orient="records", date_format="iso"))
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
