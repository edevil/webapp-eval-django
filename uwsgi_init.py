import gevent.monkey
gevent.monkey.patch_all()

import psycogreen.gevent  # noqa
psycogreen.gevent.patch_psycopg()
