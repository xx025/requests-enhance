from requests_enhance import _auto_retry_requests, _req_text, _req_json, _req_bs4soup

# demo1
# 自动重试请求
url = 'https://www.example1111.com'
re = _auto_retry_requests(url, method='GET', retry_times=2)
print(type(re), re)
# 当然也可以直接使用auto_retry_get,auto_retry_post
# re = auto_retry_get(url, retry_times=2)


# demo2
# 发送get请求并返回text
url = 'https://www.github.com'
re = _req_text(url, method='GET')
print(type(re), re)
# 当然也可以直接使用req_text_by_get,req_text_by_post
# 如 re=req_text_by_get(url)

# demo3
# 发送get请求并返回json
url = 'https://api.github.com/users/github'
re = _req_json(url, method='GET')
print(type(re), re['html_url'])
# 当然也可以直接使用req_json_by_get,req_json_by_post
# 如 re=req_json_by_get(url)

# demo4
# 发送get请求并返回bs4soup
url = 'https://www.github.com'
re = _req_bs4soup(url, method='GET')
print(type(re), re.select('title')[0].text)
# 当然也可以直接使用req_bs4soup_by_get,req_bs4soup_by_post
