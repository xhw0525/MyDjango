from django.http.request import HttpRequest


def check_siger(func):
    """Limit view to superusers only."""

    def wapper(request: HttpRequest, *args, **kwargs):
        print('--------装饰器-访问的网址--------->'.encode('utf-8'), request.get_raw_uri())

        return func(request, *args, **kwargs)

    return wapper
