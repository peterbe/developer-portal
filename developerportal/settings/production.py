from urllib.parse import urlparse

from .base import *

DEBUG = False
DEBUG_PROPAGATE_EXCEPTIONS = True
ALLOWED_HOSTS = [urlparse(BASE_URL).hostname] if BASE_URL else []

try:
    from .local import *
except ImportError:
    pass
