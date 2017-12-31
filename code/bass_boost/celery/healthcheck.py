# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)


from celery.task import control

celery_inspect = control.inspect()


def celery_ping(workers, *args, **kwargs):
    """
    Check if given celery workers are running.
    :param workers: List of workers to be checked.
    :return: Status of each worker.
    """
    try:
        ping_response = celery_inspect.ping() or None
        active_workers = ping_response.keys()
        workers_status = {w: w in active_workers for w in workers}
    except (AttributeError, OSError):
        workers_status = None
    # end try
    return workers_status