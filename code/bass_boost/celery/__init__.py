from celery import Celery
from urllib.parse import quote


# local imports
from ..secrets import CELERY_ENABLED, CELERY_WORKER, RABBITMQ_USER, RABBITMQ_PASS, RABBITMQ_HOST, RABBITMQ_VHOST

# SET UP LOGGING:
from luckydonaldUtils.logger import logging as _utils_logging
if CELERY_WORKER:
    from celery.utils.log import get_task_logger

    def _getLogger(*args,**kwargs):
        logger = get_task_logger(*args, **kwargs)
        logger.SUCCESS = _utils_logging.SUCCESS
        setattr(logger, "success", lambda message, *args: logger._log(_utils_logging.SUCCESS, message, args))
        return logger
    # end def
    getLogger = _getLogger
else:
    getLogger = _utils_logging.getLogger
# end if

logger = getLogger(__name__)

# check if we even are allowed to run
if not CELERY_ENABLED:
    raise ValueError("Celery environment variables not set. (See log)")
# end def

_celery_url = '{{scheme}}://{user}:{password}@{host}:5672'.format(
    user=quote(RABBITMQ_USER), password=quote(RABBITMQ_PASS, safe=""), host=RABBITMQ_HOST
)
if RABBITMQ_VHOST:
    _celery_url += "/" + RABBITMQ_VHOST
# end if

logger.info("Celery backend url: " + _celery_url.replace(quote(RABBITMQ_PASS, safe=""), "<PASSWORD>"))

celery = Celery(
    'bass_boost.celery.worker',  # project name
    broker=_celery_url.format(scheme="amqp"),
    # backend=_celery_url.format(scheme="rpc"),
    # include=['data.worker']
)