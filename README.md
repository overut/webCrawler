# webCrawler
## simpleCrawler
该脚本主要用来在百度图片搜索中按关键字查找，主要用到的模块包括re(正则) requests(HTTP通信用)</br>
网页是通过http get获取的图片数据，http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=' + word</br>
其中word是你要搜索的关键字，利用浏览器F12进入开发者模式观察获取网页的响应，然后解析网页获取图片地址下载即可.
## appleCrawler
现在多数网页在检索信息时，初始只提供少量的信息，需要通过滚轮获取数据</br>
F12进入开发者模式:</br>
可以发现滚轮其实触发的是新的一次http请求，查看请求参数，模拟参数pn每次递增30，ic表示过滤颜色..其他自己去试吧~
## fruitsCrawler
类似appleCrawler
