将网站上的信息转换为自己的api
========================
1、先从浏览器获取网站信息
2、转成json格式

获取头部信息
==========
从网页中获取浏览器版本信息：
'User-Agent'， requests.get

改写Content-Type
===============
把文档类型从html变为json，即为：text/html -> application/json
使用到的是flask中的jsonify方法：jsonify(XXX.json())
可省去json.dumps()复杂方法

在网址+?url=https://
==================
使用request.args.get('url')方法
访问是：/zhihu/resource?url=浏览器图片地址

获取图像文件
==========
with closing(requests.get(url, headers=header, stream=True)) as r:
    Response(r.content, mimetype = "image/jpeg")