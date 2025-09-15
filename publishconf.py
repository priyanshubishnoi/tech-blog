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

