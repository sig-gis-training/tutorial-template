# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import pydata_sphinx_theme

# -- Project information -----------------------------------------------------

project = 'Tutorial page template'
copyright = '2021, Spatial Informatics Group LLC'
author = 'Andrea Nicolau'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# extensions = ['sphinx_rtd_theme']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
#html_theme = 'sphinx_rtd_theme'
html_theme = "pydata_sphinx_theme"

# Add SIG logo
html_logo = "_static/sig-signal.png"

# Add links to social media
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/sig-gis-training",
            "icon": "fab fa-github-square",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/sig_gis",
            "icon": "fab fa-twitter-square",
        },
        {
            "name": "YouTube",
            "url": "https://www.youtube.com/channel/UC6Q-D9k-vP08-y9PS6AILWg",
            "icon": "fab fa-youtube-square",
        },
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/company/spatial-informatics-group-llc/",
            "icon": "fab fa-linkedin",
        },
        {
            "name": "Facebook",
            "url": "https://www.facebook.com/Spatial.Informatics.Group/",
            "icon": "fab fa-facebook-square",
        },
        {
            "name": "Instagram",
            "url": "https://www.instagram.com/spatial_informatics_group/",
            "icon": "fab fa-instagram-square",
        },
        {
            "name": "SIG Homepage",
            "url": "https://sig-gis.com",
            "icon": "fas fa-home",
        },        
    ],
    "favicons": [
      {
         "rel": "icon",
         "sizes": "16x16",
         "href": "favicon-16x16.png",
      },
      {
         "rel": "icon",
         "sizes": "32x32",
         "href": "favicon-32x32.png",
      },
      {
         "rel": "apple-touch-icon",
         "sizes": "180x180",
         "href": "apple-touch-icon-180x180.png"
      },
   ]
#    "collapse_navigation": True
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']