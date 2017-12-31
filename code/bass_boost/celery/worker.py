"""
This file imports the celery configuration
and the functions to be run by celery
"""

from . import celery  # pylint: disable=unused-import
from .process_audio import process_audio  # pylint: disable=unused-import