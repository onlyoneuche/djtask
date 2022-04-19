from rest_framework.routers import SimpleRouter
from core.views import ExternalRequestsViewset

data_router = SimpleRouter()
data_router.register("misc", ExternalRequestsViewset, basename="misc")