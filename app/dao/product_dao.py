from sqlalchemy import func, select, update
from app.model.product import Product
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy_crud_plus import CRUDPlus

from app.schema.product_schema import ProductCreate, ProductUpdate


class ProductDAO(CRUDPlus[Product]):

    async def count(self, session: AsyncSession) -> int:
        """
        Count all products
        :param session:
        :return:
        """
        query = await session.execute(func.count(self.model.id))
        return query.scalar()
    

    async def get_all(self, session: AsyncSession, limit: int, offset: int) -> list[Product]:
        """
        Get all products
        :param session:
        :param limit:
        :param offset:
        :return:
        """
        query = await session.execute(select(self.model).limit(limit).offset(offset))
        return query.scalars().all()


    async def create(self, session: AsyncSession, product_data : ProductCreate) -> Product:
        """
        Create product 
        :param session:
        :param product_data:
        :return:
        """

        # model_dump will turn the product_data object into a dictionary that will be passed 
        # as kwargs to the Product constructor 
        product_data= product_data.model_dump()
        product_data.update({
            "imgUrl": str(product_data.get("imgUrl"))
        })
        new_product = self.model(**product_data) # Product(**product_data)
        session.add(new_product) # This will insert the newly created product into the products table
        return new_product
    

    async def update(self, session: AsyncSession, product_id: str, product_data: ProductCreate | ProductUpdate) -> int:
        """
        Update product 
        :param session:
        :param product_id:
        :param product_data:
        :return:
        """
        # model_dump will turn the product_data object into a dictionary that will be passed 
        # as kwargs to the sqlalchemy values method

        # exclude_unset=True will exclude any fields that are not set in the product_data object
        # will keep only the fields that were specified by the user.
        product_data = product_data.model_dump(exclude_unset=True)
        if "imgUrl" in product_data:
            product_data.update({
                "imgUrl": str(product_data.get("imgUrl"))
            })
        result = await session.execute(update(self.model).where(self.model.id == product_id).values(**product_data))
        return result.rowcount


product_dao: ProductDAO = ProductDAO(Product)