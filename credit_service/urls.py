from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from .views import HealthcheckAPIView


api_urlpatterns = [
    path('api/', include(('api.urls', 'api'))),
    path('api/healthcheck', HealthcheckAPIView.as_view(), name='healthcheck'),
]

schema_view = get_schema_view(
    openapi.Info(
        title='API Credit service server',
        default_version='v1',
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
    patterns=api_urlpatterns,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    *api_urlpatterns,
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # noqa
]
