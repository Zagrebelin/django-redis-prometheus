from django.conf.urls import url
from django_redis_prometheus import exports

urlpatterns = [
    url(r'^metrics$', exports.ExportToDjangoView,
        name='prometheus-django-metrics'),
]
