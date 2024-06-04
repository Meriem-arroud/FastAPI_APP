from typing import Union
from fastapi import APIRouter, HTTPException, Response, status
from app.model.product import Product
from app.schema.pagination_schema import PaginationResponseSchema
from app.schema.product_schema import ProductCreate, ProductOut, ProductUpdate
from app.service.product_svc import product_service

router = APIRouter(prefix="/products")

@router.get("/{product_id}", status_code=status.HTTP_200_OK)
async def read_product(product_id: str, response: Response):
    try:
        product =  await product_service.get_product_info(product_id=product_id)
        if product is None:
            response.status_code= status.HTTP_404_NOT_FOUND
            return {"status": "Failed", "message": "product ID not found"}
        else : return  product 
    except Exception as e: 
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get("", status_code=status.HTTP_200_OK)
async def read_all_products(offset: int = 0, limit: int = 50):
    products_count = await product_service.get_products_count()
    products_list = await product_service.get_products_list(limit=limit, offset=offset)
    return PaginationResponseSchema(items=products_list, limit=limit, offset=offset, total=products_count)        


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_product(product_data: ProductCreate):
    try:
        new_product = await product_service.create_product(product_data=product_data)
        return {"status": "succeeded", "message": f"Product successfully created;  New product ID :{new_product.id}"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{product_id}", status_code=status.HTTP_200_OK)
async def delete_product(product_id: str):
    try:
        await product_service.delete_product(product_id=product_id)
        return {"status": "succeeded", "message": "Product successfully deleted"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.put("/{product_id}", status_code=status.HTTP_201_CREATED)
async def update_product(product_id: str, product_data: ProductCreate):
    try:
        updated_rows_count = await product_service.update_product(product_id=product_id, product_data=product_data)
        return {"status": "succeeded", "message": f"Product successfully updated! {updated_rows_count} fiels has been updated"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) 


@router.patch("/{product_id}", status_code=status.HTTP_200_OK)
async def partial_update_product(product_id: str, product_data: ProductUpdate,response:Response):
    try:
        updated_rows_count = await product_service.update_product(product_id=product_id, product_data=product_data)
        if updated_rows_count > 0:
            return {"status": "succeeded", "message": f"Product successfully updated! {updated_rows_count} fiels has been updated"}
        else:
            response.status_code=status.HTTP_404_NOT_FOUND
            return {"status": "Failed", "message": f"ID {product_id} not found in Products table"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))   




