from fastapi import APIRouter

from workshop.api.operations import router as operations_routers

router = APIRouter()
router.include_router(operations_routers)
