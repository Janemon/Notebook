import requests


# r1 = requests.get('http://httpbin.org/get')
# r2 = requests.post('http://httpbin.org/post', data={'key': 'value'})
# r3 = requests.put('http://httpbin.org/put')
# r3 = requests.delete('http://httpbin.org/delete')
# r4 = requests.head('http://httpbin.org/get')
# r5 = requests.options('http://httpbin.org/get')


# payload1 = {'key1': 'value1', 'key2': 'value2'}
# payload2 = {'key1': 'value1', 'key2': ['value2', 'value3']}
# rr1 = requests.get("http://httpbin.org/get", params=payload1)
# rr2 = requests.get("http://httpbin.org/get", params=payload2)
# print(rr1.url)
# print(rr2.url)


# Requests 会基于 HTTP 头部对响应的编码作出有根据的推测。当你访问 r.text 之时，Requests 会使用其推测的文本编码。
# rrr1 = requests.get("https://api.github.com/events")
# print(rrr1.text)  # u'[{"...."}]
# rrr1.encoding = "ISO-8859-1"
# print(rrr1.text)


# r1 = requests.get("https://api.github.com/events")
# print(r1.content)  # b'[{"..."}]
# print(r1.json())  # [u'key': {u'key':'value'...}]
# print(r1.status_code)  # check whether json successful


# get the original socket
# rr1 = requests.get("https://api.github.com/events", stream=True)
# print(rr1.raw)
# print(rr1.raw.read(10))

# Usually, we save that content into file like:
# with open(filename, 'wb') as f:
#     for chunk in r.iter_content(chunk_size):
#         f.write(chunk)


# url = "https://api.github.com/some/endpoint"
# headers = {'user-agent': 'my-app/0.0.1'}
# r1 = requests.get(url, headers=headers)


# payload1 = {'key1': 'value1', 'key2': 'value2'}  # dict
# r1 = requests.post("https://httpbin.org/post", data=payload1)
# payload2 = (('key1', 'value1'), ('key1', 'value2'))  # tublr
# r2 = requests.post("https://httpbin.org/post", data=payload2)
# payload3 = {'some': 'data'}
# r3 = requests.post("https://httpbin.org/post", json=payload3)  # string
# print(r1.text)
# print(r2.text)
# print(r3.text)


# r1 = requests.get("https://httpbin.org/get")
# print(r1.headers)
# print(r1.headers['Content-Type'])
# print(r1.headers.get('Content-Type'))


# url = 'http://example.com/some/cookie/setting/url'
# r1 = requests.get(url)
# r1.cookies['example_cookie_name']
# cookies = dict(name='value')
# r2 = requests.get(url, cookies=cookies)
# r2.text  # '{"cookies": {"name": "value}}'


# requests.get("https://github.com", timeout=0.001)


















