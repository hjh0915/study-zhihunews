import sys
sys.path.append('.')

import unittest
import app 

class TestAPP(unittest.TestCase):
    """Tester for the function patients_with_missing_values in
    treatment_functions.
    """

    def test_zhihu_news(self):
        """获取知乎新闻内容"""

        data = app.get_zhihu_news()
        print(data)

    def test_zhihu_news_by_id(self):
        """根据id获取相应的新闻具体内容"""

        nid = '9718885'
        data = app.get_zhihu_news_by_id(nid)
        print(data)

    def test_zhihu_comments_by_news_id(self):
        """根据id获取所有评论内容"""

        nid = '9718898'
        comments = app.get_zhihu_comments_by_news_id(nid)
        print(comments)

    def test_zhihu_before_news_by_date(self):
        """根据id获取前一天的新闻内容"""

        date = '20200112'
        before_news = app.get_zhihu_before_news_by_date(date)
        print(before_news)

    
if __name__ == '__main__':
    unittest.main(exit=False)