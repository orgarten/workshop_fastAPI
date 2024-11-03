from fastapi import FastAPI, status

from . import admin, catalog

app = FastAPI()


app.include_router(catalog.create_catalog_routes())
app.include_router(
    admin.create_admin_routes(),
    prefix="/admin",
    tags=["admin"]
)



