import requests

def get_json():
    response=requests.get('https://api.github.com/events')
    print(response.status_code)
    print(response.headers)
    print(response.content)
    print(response.text)
    print(response.json())

def get_proxy():
    return requests.get("http://123.207.35.36:5010/get/").content

def get_querystring():
    url='http://httpbin.org/get'
    params={
        'arg1':'value1',
        'arg2':'value2',
    }
    myip=get_proxy()
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        "Origin":myip,
    }
    response=requests.get(url,params=params,headers=headers)
    print(response.status_code)
    print(response.content)

def get_cookie():

    headers = {'User-Agent': 'Chrome'}

    url = 'http://www.douban.com'

    r = requests.get(url, headers=headers)

    print(r.status_code)

    print(r.cookies['bid'])

if __name__=='__main__':
    #get_json()
    #get_querystring()
    get_cookie()