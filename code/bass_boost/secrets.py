# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging
import os

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)


API_KEY = os.getenv('TG_API_KEY', None)
assert(API_KEY is not None)  # TG_API_KEY environment variable

URL_HOSTNAME = os.getenv('URL_HOSTNAME', None)
# can be None

URL_PATH = os.getenv('URL_PATH', None)
assert(URL_PATH is not None)  # URL_PATH environment variable

