from fastapi import APIRouter


def create_admin_routes():
    router = APIRouter()

    @router.get("/hello")
    def admin():
        return {"message": "Hello World from Admin"}

    return router