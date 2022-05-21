from fastapi import FastAPI
from .api.routers import files, analyze, items


app = FastAPI()
app.include_router(files.router, prefix="/api/v1")
app.include_router(analyze.router, prefix="/api/v1")
app.include_router(items.router, prefix="/api/v1")
