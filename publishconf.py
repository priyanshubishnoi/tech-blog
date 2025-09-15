# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = "https://priyanshubishnoi.github.io/tech-blog"
RELATIVE_URLS = False

THEME = "themes/papyrus"
THEME_STATIC_PATHS = ["static"]
THEME_STATIC_DIR = "theme"

DELETE_OUTPUT_DIRECTORY = True

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['pelican_ga4']  # keep others if you add them

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
GA4_MEASUREMENT_ID = "G-98GLR120T4"

FEED_ALL_ATOM = FEED_ALL_RSS = CATEGORY_FEED_ATOM = TAG_FEED_ATOM = None
TRANSLATION_FEED_ATOM = AUTHOR_FEED_ATOM = AUTHOR_FEED_RSS = None

# pelicanconf.py / publishconf.py
EXTRA_HEAD_DATA = """
<!-- GA4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date()); gtag('config', 'G-XXXXXXXXXX');
</script>
"""
