import requests
import json

header = {
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

def get_zhihu_news() -> str:
    """获取网站新闻内容"""

    url = "http://news-at.zhihu.com/api/4/news/latest"
    results = requests.get(url, headers=header)
    data = json.dumps(results.json(), ensure_ascii=False)

    return data

def get_zhihu_news_by_id(nid: str):
    """根据id获取相应的新闻具体内容"""

    url = "http://news-at.zhihu.com/api/4/news/" + nid
    # header['Referer'] = 'https://daily.zhihu.com'
    results = requests.get(url, headers=header)
    data = json.dumps(results.json(), ensure_ascii=False)

    return data

def get_zhihu_comments_by_news_id(nid: str) -> str:
    """根据id获取所有评论内容"""

    url = "http://news-at.zhihu.com/api/4/story/" + nid + "/comments"
    results = requests.get(url, headers=header)
    comments = json.dumps(results.json(), ensure_ascii=False)

    return comments

def get_zhihu_before_news_by_date(date: str) -> str:
    """根据id获取前一天的新闻内容"""

    url = "http://news-at.zhihu.com/api/4/news/before/" + date 
    results = requests.get(url, headers=header)
    before_news = json.dumps(results.json(), ensure_ascii=False)

    return before_news