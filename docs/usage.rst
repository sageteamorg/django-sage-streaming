Usage
-----

``django-sage-streaming`` provides two ways that you can stream videos
over HTTP: 1. built-in API View: for using built-in view add
``sage_stream.api.urls`` to urls.py

.. code:: python

    from django.urls import path, include
    urlpatterns = [
      ...
      path('api/', include('sage_stream.api.urls')),
      ...
    ]

Now you can access the stream api here:
``localhost:8000/api/stream?path=<you_video_path>``

`The settings of built-in view is available here <#settings>`__

2. create custom views: you can use stream functions in your application

.. code:: python

    from sage_stream.utils.stream_services import get_streaming_response

    response = get_streaming_response(
        path=video_path, # path to video
        range_header=range_header, # range header extracted from request
        range_re=range_re, # range header regex pattern (default is available in sage_stream.settings.STREAM_RANGE_HEADER_REGEX_PATTERN)
        max_load_volume=max_load_volume,  # the maximum volume of the response body
    )

Other functions you can use

.. code:: python

    from sage_stream.utils.file_services import file_iterator  # iterates in given file chunk by chunk in generator mode
    from sage_stream.utils.log_services import log_watch_request  # creates WatchLog instance with given data

    # usage examples

    # log
    log_watch_request(video_path, request.user.is_authenticated, ip, request.user)

    # file iterator
    resp = StreamingHttpResponse(
        file_iterator(
            path,
            offset=first_byte,
            length=length
        ),
        status=206,
        content_type=content_type
    )

Admin
-----

``django-sage-streaming`` also has logging system for watching requests

It is available in admin panel when you add ``sage_stream`` to
INSTALLED\_APPS