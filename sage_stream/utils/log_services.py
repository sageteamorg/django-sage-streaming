from sage_stream.models import WatchLog


def get_request_ip(request):
    """extract request ip"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def log_watch_request(video_path, authenticated, ip, user=None):
    """create WatchLog instance"""
    if authenticated:
        WatchLog.objects.create(
            video_path=video_path,
            is_authenticated=authenticated,
            ip=ip,
            user=user
        )
    else:
        WatchLog.objects.create(
            video_path=video_path,
            is_authenticated=authenticated,
            ip=ip
        )
