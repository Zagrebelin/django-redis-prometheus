from django.core.cache.backends import locmem

from django_redis_prometheus.cache.metrics import (
    django_cache_get_total,
    django_cache_hits_total,
    django_cache_misses_total)


class LocMemCache(locmem.LocMemCache):
    """Inherit filebased cache to add metrics about hit/miss ratio"""

    def get(self, key, default=None, version=None):
        django_cache_get_total.labels(backend='locmem').inc()
        cached = super(LocMemCache, self).get(
            key, default=None, version=version)
        if cached is not None:
            django_cache_hits_total.labels(backend='locmem').inc()
        else:
            django_cache_misses_total.labels(backend='locmem').inc()
        return cached or default
