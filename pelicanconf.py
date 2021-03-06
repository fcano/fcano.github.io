#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'fcano'
SITENAME = 'Cybersecurity Notes'
SITEURL = ''

PATH = 'content'

STATIC_PATHS = ['images']

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/florenciocano'),
          ('github', 'http://github.com/fcano'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "pelican-themes/foundation-custom"

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tag_cloud"]

