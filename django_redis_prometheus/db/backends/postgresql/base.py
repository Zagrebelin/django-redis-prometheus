import django

from django_redis_prometheus.db.common import (
    DatabaseWrapperMixin,
    ExportingCursorWrapper
)

import psycopg2.extensions
from django.db.backends.postgresql import base


class DatabaseFeatures(base.DatabaseFeatures):
    """Our database has the exact same features as the base one."""
    pass


class DatabaseWrapper(DatabaseWrapperMixin, base.DatabaseWrapper):
    def get_connection_params(self):
        conn_params = super(DatabaseWrapper, self).get_connection_params()
        conn_params['cursor_factory'] = ExportingCursorWrapper(
            psycopg2.extensions.cursor,
            self.alias,
            self.vendor,
        )
        return conn_params

    def create_cursor(self, name=None):
        # cursor_factory is a kwarg to connect() so restore create_cursor()'s
        # default behavior
        return base.DatabaseWrapper.create_cursor(self, name=name)
