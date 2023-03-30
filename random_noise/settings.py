# Scrapy settings for random_noise project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "random_noise"

SPIDER_MODULES = ["random_noise.spiders"]
NEWSPIDER_MODULE = "random_noise.spiders"
DOWNLOADER_MIDDLEWARES = {
    "random_noise.middlewares.BetterMiddleware": 543,
}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'random_noise (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True


# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
