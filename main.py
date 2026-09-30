from fastapi import FastAPI
from src.route.productRouter import productRouters
app = FastAPI(
    title="FastAPI Crash Course",
    description="We are going to learn all impotant"
)


@app.get("/")
def home():
    return { "messages" : "Welcome" }



app.include_router(productRouters, prefix="/products")

