from fastapi import APIRouter, Depends, HTTPException
from app.dependencies.gas_infra import get_gie_client
from gie import GiePandasClient
from app.models import GieBaseRequest
import json


router = APIRouter()

@router.post("/gas_storage", summary="Download gas storage data.")
async def get_gas_storage(request: GieBaseRequest, gquery: GiePandasClient = Depends(get_gie_client)):
    try:
        data = gquery.query_gas_storage(
            request.target,
            request.start_date,
            request.end_date,
        )

        result = json.loads(data.to_json(orient="records", date_format="iso"))
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/gas_company", summary="Download gas company data.")
async def get_gas_company(request: GieBaseRequest, gquery: GiePandasClient = Depends(get_gie_client)):
    try:
        data = gquery.query_gas_company(
            request.target,
            request.start_date,
            request.end_date,
        )

        result = json.loads(data.to_json(orient="records", date_format="iso"))
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/gas_country", summary="Download gas country data.")
async def get_gas_country(request: GieBaseRequest, gquery: GiePandasClient = Depends(get_gie_client)):
    try:
        data = gquery.query_gas_country(
            request.target,
            request.start_date,
            request.end_date,
        )

        result = json.loads(data.to_json(orient="records", date_format="iso"))
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/lng_terminal", summary="Download lng terminal data.")
async def get_lng_terminal(request: GieBaseRequest, gquery: GiePandasClient = Depends(get_gie_client)):
    try:
        data = gquery.query_lng_terminal(
            request.target,
            request.start_date,
            request.end_date,
        )

        result = json.loads(data.to_json(orient="records", date_format="iso"))
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/lng_lso", summary="Download lng lso data.")
async def get_lng_lso(request: GieBaseRequest, gquery: GiePandasClient = Depends(get_gie_client)):
    try:
        data = gquery.query_lng_lso(
            request.target,
            request.start_date,
            request.end_date,
        )

        result = json.loads(data.to_json(orient="records", date_format="iso"))
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/lng_country", summary="Download lng country data.")
async def get_lng_country(request: GieBaseRequest, gquery: GiePandasClient = Depends(get_gie_client)):
    try:
        data = gquery.query_lng_country(
            request.target,
            request.start_date,
            request.end_date,
        )

        result = json.loads(data.to_json(orient="records", date_format="iso"))
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
