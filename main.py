from fastapi import FastAPI
from settings import settings
from app.controller.product_controller import router as products_router

app = FastAPI(
    title=settings.TITLE,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    docs_url=settings.DOCS_URL,
    redoc_url=settings.REDOCS_URL,
    openapi_url=settings.OPENAPI_URL
)   

app.include_router(products_router)


