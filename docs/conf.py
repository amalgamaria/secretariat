# Configuration file for the Sphinx documentation builder.

import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = ‘secretariat’
copyright = ‘2019, Maria E. Adonay’
author = ‘Maria E. Adonay’
release = '0.1.0'

# -- General configuration ---------------------------------------------------

master_doc = 'index'
source_suffix = ['.rst']


extensions = ['sphinx_rtd_theme',]

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_theme_path = ["_themes" ]

