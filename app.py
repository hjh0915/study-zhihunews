import requests
import json

header = {
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

def get_zhihu_news():
    """获取网站新闻内容"""

    url = "http://news-at.zhihu.com/api/4/news/latest"
    results = requests.get(url, headers=header)
    data_str = json.dumps(results.json(), ensure_ascii=False)
    data = json.loads(data_str)

    return data

def get_zhihu_news_id(nid):
    """根据id获取相应的新闻具体内容"""

    url = "http://news-at.zhihu.com/api/4/news/" + nid
    # header['Referer'] = 'https://daily.zhihu.com'
    results = requests.get(url, headers=header)
    data = json.dumps(results.json(), ensure_ascii=False)

    return data