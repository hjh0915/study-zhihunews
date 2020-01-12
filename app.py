import requests
from flask import Flask, request
from flask import Response, jsonify
from flask_cors import CORS, cross_origin
from contextlib import closing

app = Flask(__name__)
CORS(app) # 全局API接口

header = {
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

@app.route('/zhihu/news/latest')
def get_zhihu_latest_news() -> str:
    """获取网站新闻内容"""

    url = "http://news-at.zhihu.com/api/4/news/latest"
    results = requests.get(url, headers=header)

    return jsonify(results.json())

@app.route('/zhihu/news/<nid>')
def get_zhihu_news_by_id(nid: str):
    """根据id获取相应的新闻具体内容"""

    url = "http://news-at.zhihu.com/api/4/news/" + nid
    results = requests.get(url, headers=header)

    return jsonify(results.json())

@app.route('/zhihu/comments/<nid>')
def get_zhihu_comments_by_news_id(nid: str) -> str:
    """根据id获取所有评论内容"""

    url = "http://news-at.zhihu.com/api/4/story/" + nid + "/comments"
    comments = requests.get(url, headers=header)

    return jsonify(comments.json())

@app.route('/zhihu/dates/<date>')
def get_zhihu_before_news_by_date(date: str) -> str:
    """根据id获取前一天的新闻内容"""

    url = "http://news-at.zhihu.com/api/4/news/before/" + date 
    before_news = requests.get(url, headers=header)
    # before_news = json.dumps(results.json(), ensure_ascii=False)

    return jsonify(before_news.json())

@app.route('/zhihu/resource')
def get_resource():
    url = request.args.get('url')
    header['Referer'] = 'https://daily.zhihu.com'
    # 创建上下文管理器，在执行过程离开with语句体时自动执行object.close()
    with closing(requests.get(url, headers=header, stream=True)) as r:
        return Response(r.content, mimetype = "image/jpeg")