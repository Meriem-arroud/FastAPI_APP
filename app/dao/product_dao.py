from sqlalchemy import update
from app.model.product import Product
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy_crud_plus import CRUDPlus

from app.schema.product_schema import ProductCreate, ProductUpdate


class ProductDAO(CRUDPlus[Product]):    
    async def create(self, session: AsyncSession, product_data : ProductCreate) -> Product:
        """
        Create product 
        :param session:
        :param product_data:
        :return:
        """
        product_data= product_data.model_dump()
        product_data.update({
            "imgUrl": str(product_data.get("imgUrl"))
        })
        new_product = self.model(**product_data)
        session.add(new_product)
        return new_product
    

    async def update(self, session: AsyncSession, product_id: str, product_data: ProductCreate | ProductUpdate) -> int:
        """
        Update product 
        :param session:
        :param product_id:
        :param product_data:
        :return:
        """
        product_data = product_data.model_dump(exclude_unset=True)
        if "imgUrl" in product_data:
            product_data.update({
                "imgUrl": str(product_data.get("imgUrl"))
            })
        result = await session.execute(update(self.model).where(self.model.id == product_id).values(**product_data))
        return result.rowcount


product_dao: ProductDAO = ProductDAO(Product)