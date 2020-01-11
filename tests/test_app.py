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
        for x in data['stories']:
            print(x)

    def test_zhihu_news_id(self):
        """根据id获取相应的新闻具体内容"""

        nid = '9718885'
        data = app.get_zhihu_news_id(nid)
        # print(data)

    
if __name__ == '__main__':
    unittest.main(exit=False)