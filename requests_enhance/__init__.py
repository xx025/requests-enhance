"""
它能做什么？

- 自动重试requests GET、POST请求
- 基于以上，直接获取GET、POST请求返回text属性
- 基于以上，直接获取GET、POST请求返回值转换的json类型
- 基于以上，直接获取GET、POST请求返回值转换的bs4 soup类型

自动重试时间间隔遵循2^n秒,如 1,2,4,8,16,32,64,128,256,512,1024,2048
可自定义自动重试次数，256/60= 4.26分钟

url: https://github.com/xx025/requests_enhance
"""

from .auto_retry_requests import (
    _auto_retry_requests,
    auto_retry_get,
    auto_retry_post,
    _req_json,
    req_json_by_post,
    req_json_by_get,
    _req_text,
    req_text_by_get,
    req_text_by_post
)
from .auto_retry_bs4 import (
    _req_bs4soup,
    req_bs4soup_by_get,
    req_bs4soup_by_post
)
