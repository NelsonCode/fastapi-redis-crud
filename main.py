from fastapi import FastAPI
from routes.products import routes_product


app = FastAPI()

app.include_router(routes_product, prefix="/products")