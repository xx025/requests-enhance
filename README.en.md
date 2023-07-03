# requests_enhance

Read this in other languages: [English](/README.en.md) [简体中文](/README.md)


**Why have it?**

- Sometimes we need to send GET, POST requests, but due to network reasons, the request fails, we need to retry, but the retry code is tedious
- Sometimes we request an API interface, which returns a JSON string directly, and we need to convert it to a JSON object
- Sometimes we request a web page and we need to convert it to a bs4 soup object

As above, requests_enhance is born to solve the above problems, it is based on the enhancement library of requests, its core is the encapsulation of the get, post methods of requests, so that we can use it directly to send GET, POST requests, and can automatically retry, can directly get the return value of text, json, bs4 soup objects.

**What can it do?**

- Automatically retry requests GET, POST requests 
- Based on the above, directly get the GET, POST request return text attribute 
- Based on the above, directly get the GET, POST request return value converted json type 
- Based on the above, directly get the GET, POST request return value converted bs4 soup type


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

demo1 Automatically retry get/post requests

```python
from requests_enhance import _auto_retry_requests

url = 'https://www.example1111.com'
re = _auto_retry_requests(url, method='GET', retry_times=2)
print(type(re), re)
# Of course, you can also use auto_retry_get,auto_retry_post directly
# re = auto_retry_get(url, retry_times=2)
```

demo2 Send get/post requests and return text

```python
from requests_enhance import _req_text

url = 'https://www.github.com'
re = _req_text(url, method='GET')
print(type(re), re)
# Of course,you can also use req_text_by_get,req_text_by_post directly
# 如 re=req_text_by_get(url)
```

demo3 Send get/post requests and return json

```python
from requests_enhance import _req_json

url = 'https://api.github.com/users/github'
re = _req_json(url, method='GET')
print(type(re), re['html_url'])
# Of course, you can also use req_json_by_get,req_json_by_post directly
# 如 re=req_json_by_get(url)
```

demo4 Send get/post requests and return bs4soup

```python
from requests_enhance import _req_bs4soup

url = 'https://www.github.com'
re = _req_bs4soup(url, method='GET')
print(type(re), re.select('title')[0].text)
# Of course you can also use req_bs4soup_by_get,req_bs4soup_by_post directly
```

### Use Cases

- [yanx@yzw-dl](https://github.com/xx025/yanx/blob/282d7f0bf471785ee61040f1d09a8729b90387df/yzw_dl/dl_zsyx.py#LL31C26-L31C26)

### AI Partners

- [ChatGPT](https://chat.openai.com/)
- [Copilot](https://copilot.github.com/)

### LICENSE

MIT License
