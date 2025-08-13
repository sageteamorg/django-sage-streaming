import re
import boto3
from django.conf import settings as django_settings
from rest_framework.views import APIView
from django.http import StreamingHttpResponse
from sage_stream import settings as sage_settings
from sage_stream.utils.log_services import log_watch_request, get_request_ip

class VideoStreamAPIView(APIView):
    permission_classes = sage_settings.STREAM_DEFAULT_PERMISSION_CLASSES

    def get(self, request, *args, **kwargs):
       
        max_load_volume = sage_settings.STREAM_MAX_LOAD_VOLUME
        path_key = sage_settings.STREAM_DEFAULT_VIDEO_PATH_URL_VAR
        range_re_pattern = sage_settings.STREAM_RANGE_HEADER_REGEX_PATTERN
        log_enabled = sage_settings.STREAM_WATCH_LOG_ENABLED


        s3_key = request.GET.get(path_key)

        range_header = request.META.get('HTTP_RANGE', '').strip()
        range_re = re.compile(range_re_pattern, re.I)

        if log_enabled:
            ip = get_request_ip(request)
            log_watch_request(s3_key, request.user.is_authenticated, ip, request.user)

      
        s3_client = boto3.client(
            's3',
            endpoint_url=django_settings.AWS_S3_ENDPOINT_URL,
            aws_access_key_id=django_settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=django_settings.AWS_SECRET_ACCESS_KEY,
            region_name=django_settings.AWS_S3_REGION_NAME,
        )

        s3_range = None
        if range_header:
            match = range_re.match(range_header)
            if match:
                start, end = match.groups()
                s3_range = f"bytes={start}-{end or ''}"

        s3_params = {"Bucket": django_settings.AWS_STORAGE_BUCKET_NAME, "Key": s3_key}
        if s3_range:
            s3_params["Range"] = s3_range

        s3_response = s3_client.get_object(**s3_params)

        # Build streaming HTTP response
        response = StreamingHttpResponse(
            streaming_content=s3_response["Body"].iter_chunks(chunk_size=8192),
            status=206 if s3_range else 200,
            content_type=s3_response["ContentType"]
        )

        response["Accept-Ranges"] = "bytes"
        if "ContentRange" in s3_response:
            response["Content-Range"] = s3_response["ContentRange"]
        if "ContentLength" in s3_response:
            response["Content-Length"] = str(s3_response["ContentLength"])

        return response
