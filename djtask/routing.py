from rest_framework.routers import SimpleRouter
from core.urls import data_router

v1_router = SimpleRouter(trailing_slash=False)
v1_router.registry.extend(data_router.registry)