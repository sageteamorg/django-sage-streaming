from django.urls import path

from sage_stream.api.views import VideoStreamAPIView

urlpatterns = [
    path('stream/', VideoStreamAPIView.as_view(), name='video-stream'),
]
