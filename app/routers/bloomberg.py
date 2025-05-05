from fastapi import APIRouter, Depends, HTTPException
from app.dependencies.bloomberg import bbconnect
from app.models import BDPRequest, BDHRequest, BDSRequest, BDIPRequest
from blp import blp
import json


router = APIRouter()

@router.post("/bdp", summary="Download data points.")
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


@router.post("/bdh", summary="Download time-series data.")
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


@router.post("/bds", summary="Download bulk data.")
async def get_bds(request: BDSRequest, bquery: blp.BlpQuery = Depends(bbconnect)):
    try:
        data = bquery.bds(request.tickers, request.fields, options=request.options, overrides=request.overrides)

        result = json.loads(data.to_json(orient="records", date_format="iso"))
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/bdip", summary="Download intraday bars.")
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
