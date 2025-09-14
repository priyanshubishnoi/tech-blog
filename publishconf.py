# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://priyanshubishnoi.github.io/tech-blog"
RELATIVE_URLS = False
THEME = "themes/papyrus"
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [
    'pelican_ga4',
    # ... other plugins you use
] # adjust path
GA4_MEASUREMENT_ID = "G-98GLR120T4"
# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
