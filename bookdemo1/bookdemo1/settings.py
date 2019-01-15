# -*- coding: utf-8 -*-

# Scrapy settings for bookdemo1 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'bookdemo1'

SPIDER_MODULES = ['bookdemo1.spiders']
NEWSPIDER_MODULE = 'bookdemo1.spiders'

MONGO_DB_URI='mongodb://localhost:27017/'
MONGO_DB_NAME='bookdemo1'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bookdemo1 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html

#SPIDER_MIDDLEWARES = {
    #'bookdemo1.middlewares.Bookdemo1SpiderMiddleware': None,
#}


# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'bookdemo1.middlewares.ProxySpiderMiddleware': 750,
    #'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':751,
    #'bookdemo1.middlewares.Bookdemo1DownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'bookdemo1.pipelines.Bookdemo1Pipeline': 300,
    'bookdemo1.pipelines.MongoDBPipeline':350,
    
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

HTTPERROR_ALLOWED_CODES = [521]

IP_POOLS=[
    {'address':'http://182.44.221.134:9999'},
    {'address':'http://119.101.112.52:9999'},
    {'address':'http://183.148.128.177:9999'},
    {'address':'http://171.41.84.90:9999'},
    {'address':'http://119.101.117.221:9999'},
    {'address':'http://58.55.151.239:9999'},
    {'address':'http://119.101.117.104:9999'},
    {'address':'http://171.41.84.214:9999'},
    {'address':'http://119.101.112.103:9999'},
    {'address':'http://171.41.86.209:9999'},
    {'address':'http://125.123.139.136:9999'},
    {'address':'http://119.101.116.234:9999'},
]