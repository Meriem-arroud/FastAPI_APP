from typing import Union
from fastapi import APIRouter, HTTPException, status
from app.model.product import Product
from app.schema.product_schema import ProductCreate, ProductUpdate
from app.service.product_svc import product_service

router = APIRouter(prefix="/products")

@router.get("/{product_id}")
async def read_product(product_id: str):
    return await product_service.get_product_info(product_id=product_id)


@router.get("")
async def read_all_products():
    return await product_service.get_products_list()


@router.post("/create")
async def create_product(product_data: ProductCreate):
    try:
        new_product = await product_service.create_product(product_data=product_data)
        return {"code":200, "message": f"Product successfully created;  New product ID :{new_product.id}"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{product_id}")
async def delete_product(product_id: str):
    try:
        await product_service.delete_product(product_id=product_id)
        return {"code":200, "message": "Product successfully deleted"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.put("/{product_id}")
async def update_product(product_id: str, product_data: ProductCreate):
    try:
        updated_rows_count = await product_service.update_product(product_id=product_id, product_data=product_data)
        return {"code":200, "message": f"Product successfully updated! {updated_rows_count} fiels has been updated"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) 


@router.patch("/{product_id}")
async def update_product(product_id: str, product_data: ProductUpdate):
    try:
        updated_rows_count = await product_service.update_product(product_id=product_id, product_data=product_data)
        return {"code":200, "message": f"Product successfully updated! {updated_rows_count} fiels has been updated"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))   




