from bass_boost.celery.healthcheck import celery_ping
import json
import os

hostname = os.getenv('HOSTNAME', None)
assert hostname is not None
worker_name = "celery@{host}".format(host=hostname)

print("Worker: {}".format(worker_name))

pings = celery_ping([worker_name])

success = all(p[1] for p in pings)

print(json.dumps(pings, indent=2))

exit(0 if success else 1)