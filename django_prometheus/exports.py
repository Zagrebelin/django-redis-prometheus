import logging

import prometheus_redis_client
from django.http import HttpResponse

logger = logging.getLogger(__name__)



def ExportToDjangoView(request):
    """Exports /metrics as a Django view.

    You can use django_prometheus.urls to map /metrics to this view.
    """
    registry = prometheus_redis_client.REGISTRY
    metrics_page = registry.output()
    return HttpResponse(
        metrics_page,
        content_type='text/plain; version=0.0.4; charset=utf-8'
    )