from fastapi import APIRouter, Depends, HTTPException
from app.dependencies.bloomberg import bbconnect
from app.models import BDPRequest
from blp import blp
import pandas as pd
import json


router = APIRouter()


@router.post("/", summary="Download data points.", operation_id="bdp")
async def get_bdp(request: BDPRequest, bquery: blp.BlpQuery = Depends(bbconnect)):
    try:
        data = bquery.bdp(
            request.tickers,
            request.fields,
            options=request.options,
            overrides=request.overrides,
        )

        result = json.loads(data.to_json(orient="records", date_format="iso"))
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
