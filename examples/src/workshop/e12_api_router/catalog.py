from fastapi import APIRouter, status, Body


def create_catalog_routes():
    router = APIRouter()

    @router.get(
        "/items/",
        status_code=status.HTTP_200_OK,
        tags=["catalog"],
        summary="Return items from the catalog."
    )
    async def read_items():
        return [{"id": 1, "name": "Foo", "price": 42}]

    @router.put(
        "/items/",
        status_code=status.HTTP_200_OK,
        tags=["catalog"],
        summary="Add the item to the catalog if not present."
    )
    async def put_item(name: str = Body(), price: int = Body()):
        # ...
        # code to add to catalog
        # ...
        return {"id": 1, "name": name, "price": price}

    return router