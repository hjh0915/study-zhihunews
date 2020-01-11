import requests
import json
from flask import Flask, render_template

app = Flask(__name__)

header = {
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

@app.route('/zhihu/news')
def get_zhihu_news():
    """获取网站新闻最新内容"""


    return render_template('index.html', results=data)

@app.route('/zhihu/news/<id>')
def get_zhihu_news_id(nid):
    """根据id获取相应的新闻具体内容"""
    

    return render_template('news.html', news=data)