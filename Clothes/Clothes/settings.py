# -*- coding: utf-8 -*-

# Scrapy settings for Clothes project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Clothes'

SPIDER_MODULES = ['Clothes.spiders']
NEWSPIDER_MODULE = 'Clothes.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Clothes (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Language': 'en',
#     ':authority': 's.taobao.com',
#     ':method': 'GET',
#     ':path': '/list?data-key=cat&data-value=50334016&data-action=add&ajax=true&_ksTS=1577955090892_568&callback=jsonp569&q=%E4%B8%8A%E8%A1%A3%E7%94%B7&cat=50344007&style=grid&seller_type=taobao&spm=a219r.lm895.1000187.1&cps=yes',
#     ':scheme': 'https',
#     'accept': '*/*',
#     'accept-encoding': 'gzip, deflate, br',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     'cookie': 'cna=LsMfFaGKcR8CAdodPGkf+dsL; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; miid=498335591931262502; tracknick=%5Cu5B85%5Cu660E%5Cu660E; tg=0; enc=5%2Fo5T9syTdfunYGvgHZ8pO6wXMKpF%2FTXc%2B%2BFUfFTEYcFqHtldq3gU3jAZO0DYP6juqhEvJLWrc0ZL9liAkaeLA%3D%3D; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1; _cc_=U%2BGCWk%2F7og%3D%3D; t=0d23cd76a5850436d5a1e6ca89e7e8bb; mt=ci%3D-1_0; UM_distinctid=16f4176641e1bc-05e77a2391ac09-2393f61-144000-16f4176641fad; cookie2=15a1848fc6d29f35f12bdafe435b9043; v=0; _tb_token_=5ebee07f7fe37; _m_h5_tk=f8ef0eee03a3b9147dbb94bf11dc0fb8_1577944561103; _m_h5_tk_enc=37f7194675af871f9d770d16e695a820; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; JSESSIONID=9B6547E9650A28027A902FAE7193A74F; l=dBNakX_VvATvRAkhBOfNmRz_R-Q9mpdfCsPr7BG5GICP_vfeZbOFWZcC09YwCnGV3sZvJ3Jt3efYBm8LTyUIh-WA7WIoPrd2sKYeR; isg=BF9fYXnPfRsSWnuSNO3_pV8R7rPjztauaNJrNfGjf48lgHoC-JSetnUWQlBbGIve',
#     'referer': 'https://s.taobao.com/list?q=%E4%B8%8A%E8%A1%A3%E7%94%B7&cat=50344007&style=grid&seller_type=taobao&spm=a219r.lm895.1000187.1',
#     'sec-fetch-mode': 'no-cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
# }


DEFAULT_REQUEST_HEADERS = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'acw_tc=76b20f4715779688385062929ed9600acf26efa40befde45bb0ce3a50bdde0; User_ShopSource=1; SESSION=ZDliYmRlMTUtMjU5YS00YjhlLWEzMjEtNjVlM2FjMWZmMzM5; gr_user_id=c29ef4ed-eba0-4064-9638-72e841fe7c93; a7f0bc16e8df64c1_gr_session_id=6bf32ec0-bc80-46a6-86e2-609c17d05555; a7f0bc16e8df64c1_gr_session_id_6bf32ec0-bc80-46a6-86e2-609c17d05555=true; grwng_uid=9911ebfb-f919-4a1e-aa66-9fba83444461; _ga=GA1.2.672179606.1577968842; _gid=GA1.2.1303452288.1577968842; Hm_lvt_2715ca48cf9b0d0baa75502610d0ee17=1577968843; __cfduid=df4ac9c8e183471f0460078fa1f78f5041577968840; Hm_lpvt_2715ca48cf9b0d0baa75502610d0ee17=1577969480',
    'Host': 'www.hznzcn.com',
    'Referer': 'https://www.hznzcn.com/',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'Clothes.mymiddlewares.ClothesSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'Clothes.middlewares.ClothesDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'Clothes.pipelines.ClothesPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
