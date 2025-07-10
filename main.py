from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import uuid4, UUID

app = FastAPI()

# In-memory DB simulation
products_db = {}

class Product(BaseModel):
    id: UUID | None = None
    name: str
    description: str
    price: float
    in_stock: bool

@app.post("/products/", response_model=Product)
def create_product(product: Product):
    product.id = uuid4()
    products_db[product.id] = product
    return product

@app.get("/products/", response_model=List[Product])
def get_all_products():
    return list(products_db.values())

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: UUID):
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    return products_db[product_id]

@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: UUID, updated: Product):
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    updated.id = product_id
    products_db[product_id] = updated
    return updated

@app.delete("/products/{product_id}")
def delete_product(product_id: UUID):
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    del products_db[product_id]
    return {"detail": "Product deleted"}