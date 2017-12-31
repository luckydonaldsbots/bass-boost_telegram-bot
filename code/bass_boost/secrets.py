# -*- coding: utf-8 -*-
from luckydonaldUtils.interactions import string_is_yes
from luckydonaldUtils.logger import logging
import os

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)

CELERY_WORKER = os.getenv('CELERY_WORKER', None)
if not CELERY_WORKER:
    logger.warn("Celery: $CELERY_WORKER is not set. Defaulting to `False`.\n"
                "Set it to either `yes` or `no` to remove this warning.")
    CELERY_WORKER = False
else:
    CELERY_WORKER = string_is_yes(CELERY_WORKER)
# end if

API_KEY = os.getenv('TG_API_KEY', None)
assert(API_KEY is not None)  # TG_API_KEY environment variable

URL_HOSTNAME = os.getenv('URL_HOSTNAME', None)
# can be None

URL_PATH = os.getenv('URL_PATH', None)
assert(URL_PATH is not None)  # URL_PATH environment variable

# # CELERY WORKER # #

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', None)

RABBITMQ_USER = os.getenv('RABBITMQ_USER', None)

RABBITMQ_PASS = os.getenv('RABBITMQ_PASS', None)

RABBITMQ_VHOST = os.getenv('RABBITMQ_VHOST', None)

if RABBITMQ_PASS is None or RABBITMQ_HOST is None or RABBITMQ_USER is None:
    logger.warn("Celery: One of the following environment variables is empty:\n"
                + (", ".join("${k} ({v!r})".format(k=k,v=globals()[k]) for k in ["RABBITMQ_HOST", "RABBITMQ_USER", "RABBITMQ_PASS"]))
                + "\nYou won't be able to run celery like this."
    )
    CELERY_ENABLED = False
else:
    CELERY_ENABLED = True
# end if