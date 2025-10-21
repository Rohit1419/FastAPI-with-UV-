from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class ProductBase(BaseModel):
    
    title : str = Field(..., min_length = 1, max_length=200)
    description : Optional[str] = Field(None, max_length=1000) 
    price : float = Field(..., gt=0)
    quantity : int = Field(..., ge=0)
    category : Optional[str] = Field(None, max_length=100)
    image_url : Optional[str] = Field(None)


class ProductCreate(ProductBase):

    pass 

class ProductUpdate(BaseModel):
    title : Optional[str] = Field(None, min_length = 1, max_length=200)
    description : Optional[str] = Field(None, max_length=1000) 
    price : Optional[float] = Field(None, gt=0)
    quantity : Optional[int] = Field(None, ge=0)
    category : Optional[str] = Field(None, max_length=100)
    image_url : Optional[str] = Field(None)

class ProductResponse(ProductBase):

    id : int 
    is_active : bool
    created_at : datetime 
    updated_at : Optional[datetime] = None

    class Config:
        from_attributes = True

class ProductListResponse(BaseModel):
    products : List[ProductResponse]
    total : int 
    page : int
    size : int
    pages : int


