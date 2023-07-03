import time

import requests


def _auto_retry_requests(url, method='GET', retry_times=8, **kwargs):
    """

    :param url: 要请求的url
    :param method: 要使用的请求方法,默认为get
    :param retry_times: 重试最大次数,默认为8次
    :param kwargs: 要传入的其他参数,如headers,data等
    :return:
    """

    # 自动重试次数
    retry_count = 0

    # 自动重试时间间隔
    retry_interval = 1

    assert method in ['GET', 'POST'], 'method must be GET or POST'

    request_method = requests.get
    if method == 'GET':
        pass
    elif method == 'POST':
        request_method = requests.post

    # 自动重试
    while retry_count < retry_times:
        try:
            response = request_method(url, **kwargs)
            return response
        except Exception as e:
            retry_count += 1
            retry_interval *= 2
            print('第{}次自动重试,错误信息:{}'.format(retry_count, e))
            time.sleep(retry_interval)
    return None


def auto_retry_get(url, retry_times=8, **kwargs):
    return _auto_retry_requests(url, method='GET', retry_times=retry_times, **kwargs)


def auto_retry_post(url, retry_times=8, **kwargs):
    # 自动重试post请求
    return _auto_retry_requests(url, method='POST', retry_times=retry_times, **kwargs)


def _req_json(url, method='GET', retry_times=8, **kwargs):
    """
    自动将请求数据转换成json格式

    :param url:
    :param method:
    :param retry_times:
    :param kwargs:
    :return:
    """
    assert method in ['GET', 'POST'], 'method must be GET or POST'

    method = auto_retry_get
    if method == 'GET':
        pass
    elif method == 'POST':
        method = auto_retry_post

    response = method(url, retry_times=retry_times, **kwargs)
    if response is None:
        return None
    try:
        return response.json()
    except Exception as e:
        print('auto_retry_get_to_dict error:{}'.format(e))
        return None


def req_json_by_post(url, retry_times=8, **kwargs):
    """
    发送post请求，自动将请求数据转换成json格式

    :param url:
    :param retry_times:
    :param kwargs:
    :return:
    """

    return _req_json(url, method='POST', retry_times=retry_times, **kwargs)

def req_json_by_get(url, retry_times=8, **kwargs):
    """
    发送get请求，自动将请求数据转换成json格式

    :param url:
    :param retry_times:
    :param kwargs:
    :return:
    """

    return _req_json(url, method='GET', retry_times=retry_times, **kwargs)

def _req_text(url, method='GET', retry_times=8, **kwargs):
    # 自动获取请求内容的content.text
    assert method in ['GET', 'POST'], 'method must be GET or POST'

    method = auto_retry_get
    if method == 'GET':
        pass
    elif method == 'POST':
        method = auto_retry_post

    response = method(url, retry_times=retry_times, **kwargs)
    if response is None:
        return None
    try:
        return response.text
    except Exception as e:
        print('auto_retry_requests_text error:{}'.format(e))
        return None


def req_text_by_get(url, retry_times=8, **kwargs):
    # 发送get请求，回去content.text
    """
    发送get请求，回去content.text

    :param url:
    :param retry_times:
    :param kwargs:
    :return:
    """
    return _req_text(url, method='GET', retry_times=retry_times, **kwargs)


def req_text_by_post(url, retry_times=8, **kwargs):
    """
    发送post请求，回去content.text

    :param url:
    :param retry_times:
    :param kwargs:
    :return:
    """

    return _req_text(url, method='POST', retry_times=retry_times, **kwargs)
