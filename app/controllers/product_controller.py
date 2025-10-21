from sqlalchemy.orm import Session
from models.product_model import Product
from schemas.product_schema import ProductCreate, ProductUpdate
from typing import List, Optional
from fastapi import HTTPException, status


class ProductController:

    @staticmethod
    def create_product(db:Session, product_data : ProductCreate) ->Product:

        
        new_product = Product(**product_data.model_dump())

        db.add(new_product)
        db.commit()
        db.refresh(new_product)

        return new_product

    @staticmethod
    def get_product_by_id(db:Session, product_id : int) ->  Product:

        product = db.query(Product).filter(product_id == Product.id).first()

        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
        
        return product
    
    @staticmethod
    def get_all_products(db:Session, skip:int=0, category : Optional[str]=None, limit:int=100) -> List[Product]:

        products = db.query(Product).filter(Product.is_active == True)

        if category:
            products = products.filter(Product.category.ilike(f"%{category}%"))

        return products.offset(skip).limit(limit).all()
    
    @staticmethod
    def update_product(db:Session, product_id : int , product_data :ProductUpdate ) -> Product:

        product = ProductController.get_product_by_id(db, product_id)

        update_data = product_data.model_dump(exclude_unset=True)

        for field , value in update_data.items():
            setattr(product, field, value)

        
        db.commit()
        db.refresh(product)

        return product  
    

    @staticmethod
    def delete_product(db:Session, product_id : int) -> None:

        product = ProductController.get_product_by_id(db, product_id)

        product.is_active = False

        db.commit()
        return {"Message" : "Product deleted successfully"}
    
    @staticmethod
    def delete_product_hard(db:Session, product_id : int) -> None:

        product = ProductController.get_product_by_id(db, product_id)

        db.delete(product)
        db.commit()

        return {"Message" : "Product permanently deleted successfully"}
    
    @staticmethod
    def get_products_count(db:Session, category : Optional[str] =None) -> int:

        products = db.query(Product).filter(Product.is_active == True)

        if category:
            products = products.filter(Product.category.ilike(f"%{category}%"))

        return products.count()
    

