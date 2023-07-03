from .auto_retry_requests import _req_text


def _req_bs4soup(url, method='GET', retry_times=8, **kwargs):
    """
    发送get请求，回去BeautifulSoup对象

    :param url:
    :param retry_times:
    :param kwargs:
    :return:
    """

    assert method in ['GET', 'POST'], 'method must be GET or POST'

    text = _req_text(url, method=method, retry_times=retry_times, **kwargs)
    if text is None:
        return None
    try:
        from bs4 import BeautifulSoup
        return BeautifulSoup(text, 'html.parser')
    except Exception as e:
        print('req_bs4soup error:{}'.format(e))
        return None


def req_bs4soup_by_get(url, retry_times=8, **kwargs):
    """
    发送get请求，回去BeautifulSoup对象

    :param url:
    :param retry_times:
    :param kwargs:
    :return:
    """
    return _req_bs4soup(url, method='GET', retry_times=retry_times, **kwargs)


def req_bs4soup_by_post(url, retry_times=8, **kwargs):
    """
    发送post请求，回去BeautifulSoup对象

    :param url:url
    :param retry_times: 重试次数
    :param kwargs: bs4soup对象
    :return:
    """
    return _req_bs4soup(url, method='POST', retry_times=retry_times, **kwargs)
