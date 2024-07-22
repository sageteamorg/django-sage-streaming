# Django Sage Streaming
#### django-sage-streaming is a package based on Django Web Framework & Django Rest Framework for video streaming.

##### The Latest version of [django-sage-streaming](https://django-sage-streaming.readthedocs.io/) documentation

![SageTeam](https://github.com/sageteam-org/django-sage-painless/blob/develop/docs/images/tag_sage.png?raw=true "SageTeam")

![PyPI release](https://img.shields.io/pypi/v/django-sage-streaming "django-sage-streaming")
![Supported Python versions](https://img.shields.io/pypi/pyversions/django-sage-streaming "django-sage-streaming")
![Supported Django versions](https://img.shields.io/pypi/djversions/django-sage-streaming "django-sage-streaming")
![Documentation](https://img.shields.io/readthedocs/django-sage-streaming "django-sage-streaming")

- [Project Detail](#project-detail)
- [installation](#installation)
- [Get Started](#getting-started)
- [Admin](#admin)
- [Settings](#settings)
- [Front-End implementation](#frontend)

## Project Detail

You can find all technologies we used in our project into these files:
* Version: 1.0.0
* Frameworks:
  - Django 3.2.5
* Libraries:
  - Django rest framework 3.12.4
* Language: Python 3.9.4

## Installation

First install package

```shell
$ pip install django-sage-streaming
```

Then add `sage_stream` to INSTALLED_APPS in settings.py

```python
INSTALLED_APPS = [
  ...
  'sage_stream',
  ...
]
```

Also make sure you have `rest_framework` in INSTALLED_APPS

```python
INSTALLED_APPS = [
  ...
  'rest_framework',
  ...
]
```

## Getting Started

`django-sage-streaming` provides two ways that you can stream videos over HTTP:
1. built-in API View: for using built-in view add `sage_stream.api.urls` to urls.py

```python
from django.urls import path, include
urlpatterns = [
  ...
  path('api/', include('sage_stream.api.urls')),
  ...
]
```

Now you can access the stream api here: `localhost:8000/api/stream?path=<you_video_path>`

[The settings of built-in view is available here](#settings)

2. create custom views: you can use stream functions in your application

```python
from sage_stream.utils.stream_services import get_streaming_response

response = get_streaming_response(
    path=video_path, # path to video
    range_header=range_header, # range header extracted from request
    range_re=range_re, # range header regex pattern (default is available in sage_stream.settings.STREAM_RANGE_HEADER_REGEX_PATTERN)
    max_load_volume=max_load_volume,  # the maximum volume of the response body
)
```

Other functions you can use

```python
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
```

## Admin
`django-sage-streaming` also has logging system for watching requests

It is available in admin panel when you add `sage_stream` to INSTALLED_APPS

## Settings

Here are the parameters that you can set from setting:

| Parameter                                    | Description                                                                      |
| -------------------------------------------- |:--------------------------------------------------------------------------------:|
| STREAM_DEFAULT_PERMISSION_CLASSES            | permission_classes that used in built-in APIView. default: (AllowAny,)           |
| STREAM_DEFAULT_VIDEO_PATH_URL_VAR            | url path variable key. default: path                                             |
| STREAM_MAX_LOAD_VOLUME                       | maximum load video in each chunk(by MB). default: 8                              |
| STREAM_WATCH_LOG_ENABLED                     | is log watch requests enabled. default: True                                     |
| STREAM_RANGE_HEADER_REGEX_PATTERN            | range header regex pattern. default: r'bytes\s*=\s*(\d+)\s*-\s*(\d*)'            |

## Frontend
Frontend implementation is so easy

you just need to add stream url as `src` in `video` tag

```html
<video width="480" controls>
    <source src="http://localhost:8000/api/stream/?path=<path_to_video>" type="video/mp4">
</video>
```
