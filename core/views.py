import requests
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response


from .serializers import DataSerializer
from .tasks import get_data

class ExternalRequestsViewset(GenericViewSet):
    permission_classes = [AllowAny]

    @action(methods=['post'], detail=False, url_path='data', url_name='data')
    def process_data(self, request, *args, **kwargs):
        serializer = DataSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        data = serializer.data
        try:
            _ = get_data.delay(data)
        except Exception as e:
            return Response({"error": str(e)}, status=400)
        return Response({"message": "processing your request"})