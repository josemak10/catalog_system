from fastapi import FastAPI
from users.routers import router as router_user
from products.routers import router as router_products

app = FastAPI()
app.include_router(router_user)
app.include_router(router_products)
