from rest_framework.routers import SimpleRouter

from core.views import UserViewSet


plan_router = SimpleRouter()
plan_router.register('users/', UserViewSet, basename='users')