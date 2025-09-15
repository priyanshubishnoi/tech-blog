AUTHOR = 'Priyanshu Bishnoi'
SITENAME = 'BishnoiBytes'
SITEURL = ""
RELATIVE_URLS = True
DIRECT_TEMPLATES = [
    'index',
    'tags',
    'categories',
    'authors',
    'search',
    'archives',   # this enables dates archive
    'analytics'
]

PATH = "content"

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)
THEME = "themes/papyrus"
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['pelican_ga4']
SEARCH_MODE = "output"
SEARCH_HTML_SELECTOR = "article"  
GA4_MEASUREMENT_ID = "G-98GLR120T4"
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


FEED_ALL_ATOM = FEED_ALL_RSS = CATEGORY_FEED_ATOM = TAG_FEED_ATOM = None
TRANSLATION_FEED_ATOM = AUTHOR_FEED_ATOM = AUTHOR_FEED_RSS = None

EXTRA_HEAD_DATA = """
<!-- GA4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date()); gtag('config', 'G-XXXXXXXXXX');
</script>
"""
