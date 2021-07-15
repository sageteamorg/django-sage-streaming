import mimetypes
import os
from wsgiref.util import FileWrapper

from django.http import StreamingHttpResponse

from sage_stream.utils.file_services import file_iterator


def get_first_byte(first_byte=None):
    """get first byte"""
    return int(first_byte) if first_byte else 0


def get_last_byte(first_byte, max_load_volume):
    """get last byte"""
    return first_byte + 1024 * 1024 * max_load_volume


def get_length(first_byte, last_byte):
    """get bytes length"""
    return last_byte - first_byte + 1


def get_content_range_header(first_byte, last_byte, size):
    """create Content-Range header"""
    return 'bytes %s-%s/%s' % (first_byte, last_byte, size)


def get_streaming_response(path, range_header, range_re, max_load_volume):
    """
    get range_header and match bytes position in the file
    generate StreamingHttpResponse
    """
    range_match = range_re.match(range_header)
    size = os.path.getsize(path)
    content_type, encoding = mimetypes.guess_type(path)
    content_type = content_type or 'application/octet-stream'
    if range_match:
        first_byte, last_byte = range_match.groups()
        first_byte = get_first_byte(first_byte)
        last_byte = get_last_byte(first_byte, max_load_volume)
        if last_byte >= size:
            last_byte = size - 1
        length = get_length(first_byte, last_byte)
        resp = StreamingHttpResponse(
            file_iterator(
                path,
                offset=first_byte,
                length=length
            ),
            status=206,
            content_type=content_type
        )
        resp['Content-Length'] = str(length)
        resp['Content-Range'] = get_content_range_header(first_byte, last_byte, size)
    else:
        # when the video stream is not obtained, the entire file is returned in the generator mode to save memory.
        resp = StreamingHttpResponse(
            FileWrapper(open(path, 'rb')),
            content_type=content_type
        )
        resp['Content-Length'] = str(size)
        resp['Accept-Ranges'] = 'bytes'
    return resp
