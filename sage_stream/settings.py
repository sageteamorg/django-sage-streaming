from django.conf import settings
from rest_framework.permissions import AllowAny

STREAM_DEFAULT_PERMISSION_CLASSES = getattr(settings, 'STREAM_DEFAULT_PERMISSION_CLASSES', (AllowAny,))
STREAM_DEFAULT_VIDEO_PATH_URL_VAR = getattr(settings, 'STREAM_DEFAULT_VIDEO_PATH_URL_VAR', 'path')
STREAM_MAX_LOAD_VOLUME = getattr(settings, 'STREAM_MAX_LOAD_VOLUME', 8)
STREAM_WATCH_LOG_ENABLED = getattr(settings, 'STREAM_WATCH_LOG_ENABLED', True)
STREAM_RANGE_HEADER_REGEX_PATTERN = getattr(settings, 'STREAM_RANGE_HEADER_REGEX_PATTER', r'bytes\s*=\s*(\d+)\s*-\s*(\d*)')
