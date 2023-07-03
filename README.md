# requests_enhance

Read this in other languages: [English](/README.en.md) [简体中文](/README.md)

**为什么有它？**

- 有时候我们需要发送GET、POST请求，但是由于网络原因，请求失败，我们需要重试，但是重试的代码很繁琐
- 有时候我们请求的是API 接口, 它直接返回JSON字符串，我们需要将其转换为JSON对象
- 有时候我们请求的是网页，我们需要将其转换为bs4 soup对象

如上，requests_enhance就是为了解决以上问题而生的，它是基于requests的增强库，它的核心是对requests的get、post方法进行了封装，使得我们可以直接使用它来发送GET、POST请求，并且可以自动重试，可以直接获取返回值的text、json、bs4 soup对象。

**它能做什么？**

- 自动重试requests GET、POST请求
- 基于以上，直接获取GET、POST请求返回text属性
- 基于以上，直接获取GET、POST请求返回值转换的json类型
- 基于以上，直接获取GET、POST请求返回值转换的bs4 soup类型


## Usage

```shell
pip install --upgrade git+https://github.com/xx025/requests_enhance.git
```

```python
from requests_enhance import _auto_retry_requests

url = 'https://www.example1111.com'
re = _auto_retry_requests(url, method='GET', retry_times=2)
print(type(re), re)
```


## API

demo1 自动重试get/post请求

```python
from requests_enhance import _auto_retry_requests

url = 'https://www.example1111.com'
re = _auto_retry_requests(url, method='GET', retry_times=2)
print(type(re), re)
# 当然也可以直接使用auto_retry_get,auto_retry_post
# re = auto_retry_get(url, retry_times=2)
```

demo2 发送get/post请求并返回text

```python
from requests_enhance import _req_text

url = 'https://www.github.com'
re = _req_text(url, method='GET')
print(type(re), re)
# 当然也可以直接使用req_text_by_get,req_text_by_post
# 如 re=req_text_by_get(url)
```

demo3 发送get/post请求并返回json

```python
from requests_enhance import _req_json

url = 'https://api.github.com/users/github'
re = _req_json(url, method='GET')
print(type(re), re['html_url'])
# 当然也可以直接使用req_json_by_get,req_json_by_post
# 如 re=req_json_by_get(url)
```

demo4 发送get/post请求并返回bs4soup

```python
from requests_enhance import _req_bs4soup

url = 'https://www.github.com'
re = _req_bs4soup(url, method='GET')
print(type(re), re.select('title')[0].text)
# 当然也可以直接使用req_bs4soup_by_get,req_bs4soup_by_post
```


### 使用案例

- [yanx@yzw-dl](https://github.com/xx025/yanx/blob/282d7f0bf471785ee61040f1d09a8729b90387df/yzw_dl/dl_zsyx.py#LL31C26-L31C26)

### AI合作伙伴

- [ChatGPT](https://chat.openai.com/)
- [Copilot](https://copilot.github.com/)

### LICENSE

MIT License
