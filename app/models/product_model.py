from sqlalchemy import Column, Integer, String, Float, DateTime , Text
from app.config.database import Base
from sqlalchemy.sql import func

class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True),
    title = Column(String, nullable= False, index = True),
    description = Column(Text,   nullable= True),
    price = Column(Float, nullable= False),
    quantity = Column(Integer, nullable= False, default=0),
    category = Column(String, nullable= True),
    image_url = Column(String, nullable= True),
    created_at = Column(DateTime(timezone=True), server_default=func.now()),
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()),


    def __repr__(self):
        return f"<Product (id = '{self.id}' , title = '{self.title}', price = '{self.price}'  >"

    