from fastapi import APIRouter, HTTPException, BackgroundTasks
from src.utils.utils import get_all_product, create_all_product, send_email
from src.DTO.product_schema import CreateProduct,UpdateProduct, OrderSchema


productRouters = APIRouter()


@productRouters.get("/")
def get_all_products(product_id:int = None):
    allProduct = get_all_product()

    if not product_id:
        return allProduct
    
    for product in allProduct:
           if product['id'] == product_id:
               return product
    return HTTPException(status_code=400, detail={"error":"Product not found for this ID"})
   
@productRouters.get("/{id}")
def getOneProduct(id:int):
    allProduct = get_all_product()
    for product in allProduct:
        if product['id'] == id:
            return product
    return HTTPException(status_code=400, detail={"error":"Product not found for this ID"})


@productRouters.post("/create")
def create_product(product: CreateProduct):

    products = get_all_product()

    next_id = max(
        [product["id"] for product in products],
        default=0
    ) + 1

    new_product = {
        "id": next_id,
        "name": product.name,
        "price": product.price,
        "category": product.category,
        "stock": product.stock
    }

    products.append(new_product)

    create_all_product(products)

    return {
        "message": "New Product Created Successfully",
        "product": new_product
    }


@productRouters.put("/update/{id}")
def updateProduct(product: UpdateProduct, id: int):

    allProducts = get_all_product()

    for index, p in enumerate(allProducts):

        if p["id"] == id:

            changes = {}

            for k, v in product.model_dump().items():
                if v is not None:
                    changes[k] = v

            allProducts[index] = {
                "id": id,
                **p,
                **changes
            }

            create_all_product(allProducts)

            return {
                "message": "Product Updated Successfully",
                "product": allProducts[index]
            }

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )


@productRouters.delete("/delete/{id}")
def deleteProduct(id: int):

    allProducts = get_all_product()

    for index, p in enumerate(allProducts):

        if p["id"] == id:

            deleted_product = allProducts.pop(index)

            create_all_product(allProducts)

            return {
                "message": "Product Deleted Successfully",
                "product": deleted_product
            }

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )

@productRouters.post("/order")
async def placeOrder(OrderDetails:OrderSchema, BgTask:BackgroundTasks):
    count = OrderDetails.count
    product_id = OrderDetails.product_id
    email = OrderDetails.email

    print(product_id, OrderDetails)

    oneProduct = None
    allProducts = get_all_product()

    for index, p in enumerate(allProducts):
        if p["id"] == product_id:
            oneProduct = p
            break

    if not oneProduct:
        raise HTTPException(
        status_code=404,
        detail="Product ID Not found"
)

    if oneProduct['stock'] < count:
        return HTTPException(status_code=400, detail={"error":"Product out of stock"})

    BgTask.add_task(send_email, email)

    return{"message":"Order Place Successfully"}







