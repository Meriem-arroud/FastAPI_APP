from typing import Union
from fastapi import FastAPI
from fastapi_pagination import add_pagination
from settings import settings
from app.controller.product_controller import router as products_router
from app.service.product_svc import product_service

app = FastAPI(
    title=settings.TITLE,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    docs_url=settings.DOCS_URL,
    redoc_url=settings.REDOCS_URL,
    openapi_url=settings.OPENAPI_URL,
    #default_response_class=MsgSpecJSONResponse,
    #lifespan=register_init,
)

@app.get("/")
def hellomsg():
    return {"message": "Hellow world!"}

add_pagination(app)    

app.include_router(products_router)


