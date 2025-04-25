from fastapi import FastAPI
from app.routers.bdp_router import router as bdp_router
from app.routers.bdh_router import router as bdh_router
from app.routers.bds_router import router as bds_router
from app.routers.bdip_router import router as bdip_router

tags_metadata = [
    {
        "name": "query",
        "description": "Endpoints for querying Bloomberg data.",
    }
]

app = FastAPI(
    title="BBMirror",
    description="API providing access to financial data using the blp Python library.",
    version="1.0.0",
    openapi_tags=tags_metadata,
    docs_url="/",
)

app.include_router(bdp_router, prefix="/bdp", tags=["query"])
app.include_router(bdh_router, prefix="/bdh", tags=["query"])
app.include_router(bds_router, prefix="/bds", tags=["query"])
app.include_router(bdip_router, prefix="/bdip", tags=["query"])