from scrapy import signals
from selenium import webdriver
from scrapy.http import HtmlResponse
driver = webdriver.PhantomJS(
    executable_path=r'F:\Python\train\forth\phantomjs-2.1.1-windows\bin\phantomjs.exe')


class ClothesSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        url = request.url
        driver.get(url=url)

        response = driver.page_source
        return HtmlResponse(url=url, body=response, encoding='utf-8')
