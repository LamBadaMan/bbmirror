from fastapi import FastAPI
from app.routers.bloomberg import router as bloomberg
from app.routers.gas_infra import router as gie


app = FastAPI(
    title="fastdata",
    description="API providing access to several data sources.",
    version="1.0.0",
    docs_url="/",
)

app.include_router(bloomberg, tags=["Bloomberg"])
app.include_router(gie, tags=["GIE"])
