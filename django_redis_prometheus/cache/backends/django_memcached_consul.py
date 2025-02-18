from __future__ import absolute_import

from django_redis_prometheus.cache.metrics import (
    django_cache_get_total,
    django_cache_hits_total,
    django_cache_misses_total)

from django_memcached_consul import memcached


class MemcachedCache(memcached.MemcachedCache):
    """Inherit django_memcached_consul to add metrics about hit/miss ratio"""

    def get(self, key, default=None, version=None):
        django_cache_get_total.labels(backend='django_memcached_consul').inc()
        cached = super(MemcachedCache, self).get(
            key, default=None, version=version)
        if cached is not None:
            django_cache_hits_total.labels(
                backend='django_memcached_consul').inc()
        else:
            django_cache_misses_total.labels(
                backend='django_memcached_consul').inc()
        return cached or default
