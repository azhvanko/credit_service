from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


__all__ = (
    'HealthcheckAPIView',
)


class HealthcheckAPIView(APIView):
    authentication_classes = ()

    @staticmethod
    def get(*_) -> Response:
        return Response(status=status.HTTP_200_OK)
