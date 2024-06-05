from fastapi.encoders import jsonable_encoder
from app.dao.product_dao import product_dao
from app.helpers.redis_cache import cache
from app.model.product import Product
from app.schema.product_schema import ProductCreate, ProductUpdate
from database.db_postgress import async_session


class ProductService:
    @staticmethod
    @cache(ttl=60)
    async def get_product_info(product_id: str) -> Product:
        async with async_session.begin() as session:
            product = await product_dao.select_model_by_id(session, pk=product_id)
            return jsonable_encoder(product)     

    @staticmethod
    @cache(ttl=60)
    async def get_products_count() -> int:
        async with async_session.begin() as session:
            products_count = await product_dao.count(session)
            return products_count       


    @staticmethod
    @cache(ttl=60)
    async def get_products_list(limit: int, offset: int) -> list[Product]:
        async with async_session.begin() as session:
            products_list = await product_dao.get_all(session, limit, offset)
            return jsonable_encoder(products_list)     
          

    @staticmethod
    async def create_product(product_data: ProductCreate) -> Product:       
         async with async_session.begin() as session:
            new_product = await product_dao.create(session, product_data=product_data)
            return new_product


    @staticmethod
    async def delete_product(product_id: str) -> None:
        async with async_session.begin() as session:
            await product_dao.delete_model(session, pk=product_id)  


    @staticmethod
    async def update_product(product_id: str, product_data: ProductUpdate)-> int:
        async with async_session.begin() as session:
            updated_rows_count = await product_dao.update(session, product_id=product_id, product_data=product_data)  
            return updated_rows_count
        

product_service = ProductService()