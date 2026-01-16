from fastapi import FastAPI,HTTPException,Query,Path
from service.products import load_products


app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/products")
def get_products(): 
    return load_products()

@app.get("/product")
def list_products(
#     dep=Depends(load_products),
    name: str = Query(
        default=None,
        min_length=1,
        max_length=50,
        description="Search by product name (case insensitive)",
        example="Energy 3Pcs",
    ),
    sort_by_price: bool = Query(default=False, description="Sort products by price"),
    order: str = Query(
        default="asc", description="Sort order when sort_by_price=true (asc,desc)"
    ),
    limit: int = Query(
        default=10,
        ge=1,
        le=100,
        description="Number of items to return",
    ),
    offset: int = Query(
        default=0,
        ge=0,
        description="Pagination Offset",
)):


    products = get_products()
    # products = dep

    if name:
        needle = name.strip().lower()
        products = [p for p in products if needle in p.get("name", "").lower()]

    if not products:
        raise HTTPException(
            status_code=404, detail=f"No product found matching name={name}"
        )

    if sort_by_price:
        reverse = order == "desc"
        products = sorted(products, key=lambda p: p.get("price", 0), reverse=reverse)

    total = len(products)
    products = products[offset : offset + limit]
    return {"total": total, "limit": limit, "items": products}


@app.get("/products/{product_id}")
def get_product_by_id(product_id:str=Path(...,min_length=36,max_length=36,description="UUID of the products")):
    products=get_products()
    product=next((p for p in products if str(p.get("id"))==product_id),None)
    if not product:
        raise HTTPException(status_code=400,detail=f"Product with id={product_id} not found ")
    return product 