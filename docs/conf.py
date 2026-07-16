# Configuration file for the Sphinx documentation builder.

project = 'Ancestry Login Guide'
author = 'Ancestry Guide'
release = '1.0'

# Extensions
extensions = [
    'sphinx_sitemap',
]

# Templates
templates_path = ['_templates']

exclude_patterns = []

# Theme
html_theme = 'alabaster'

# Static files
html_static_path = ['_static']

# Language
language = 'en'

# Browser Title
html_title = "Ancestry.com Login Guide 2026"

# Sitemap
html_baseurl = "https://login-ancestrycom-login.readthedocs-hosted.com/en/latest/"
sitemap_url_scheme = "{link}"
