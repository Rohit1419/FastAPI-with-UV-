from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.config.database import get_db
from app.controllers.product_controller import ProductController
from app.schema.product_schema import ProductResponse, ProductCreate, ProductUpdate

router = APIRouter(
    prefix="/products",
    tags=["Products"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=ProductResponse, status_code=201)
async def create_product(
    product : ProductCreate,
    db : Session = Depends (get_db)
):
    return ProductController.create_product(db, product)

@router.get("/{product_id}", response_model=ProductResponse, status_code=200 )
async def get_product_by_id(
    product_id : int,
    db:Session = Depends (get_db)
):
    return ProductController.get_product_by_id(db, product_id)


@router.get("/", response_model=List[ProductResponse], status_code=200)

async def get_all_products(
    skip: int = Query(0, ge=0, description="Number of products to skip"),
    limit: int = Query(10, ge=1, le=100, description="Number of products to return"),
    category: Optional[str] = Query(None, description="Filter by category"),
    db: Session = Depends(get_db)
):
    products =  ProductController.get_all_products(db, skip, category, limit)
    return products


@router.put("/{product_id}", response_model=ProductResponse, status_code=200)
async def update_product(
    product_id : int,
    product : ProductUpdate,
    db : Session = Depends (get_db)

):
    return ProductController.update_product(db, product_id, product)



@router.delete("/{product_id}", status_code=204)
async def delete_product(
    product_id : int,
    db : Session = Depends (get_db)
):
    ProductController.delete_product(db, product_id)
    return None

@router.delete("/{product_id}/hard", status_code=204)
async def delete_product_hard(
    product_id : int,
    db : Session = Depends (get_db)
):
    ProductController.delete_product_hard(db, product_id)
    return None







