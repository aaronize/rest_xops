from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path(r'', include('apps.rbac.urls')),
    path(r'', include('apps.cmdb.urls')),
    path(r'', include('apps.deployment.urls')),
    path('docs/', include_docs_urls()),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
