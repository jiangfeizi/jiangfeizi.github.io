AUTHOR = 'Tom'
SITENAME = "Tom's life"
SITEURL = 'https://jiangfeizi.github.io/'
TIMEZONE = 'Asia/Shanghai'
LOCALE = "zh_CN.utf8"

THEME = "/root/pelican-themes/elegant"

PATH = 'content'
RELATIVE_URLS = True

STATIC_PATHS = ['images']

LOAD_CONTENT_CACHE = False
DISPLAY_PAGES_ON_MENU = False

ENCRYPT_CONTENT = {
    'title_prefix': '[Encrypted]',
    'summary': 'This content is encrypted.'
}


DEFAULT_LANG = 'en'
USE_FOLDER_AS_CATEGORY = True
SLUGIFY_SOURCE = 'title'
DEFAULT_DATE = 'fs'
FILENAME_METADATA = '(?P<title>.*)'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
GITHUB_URL = 'https://github.com/jiangfeizi'
# LINKS = (('GitHub', 'https://github.com/jiangfeizi'),)

DEFAULT_PAGINATION = 10
PORT = 6006

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True