# Configuration file for the Sphinx documentation builder.

import os
import sys
import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------

project = 'secretariat'
copyright = '2020, `Maria E. Adonay`_'
author = 'Maria E. Adonay'
release = '0.1.0'

# -- General configuration ---------------------------------------------------

templates_path = ['_templates']
exclude_patterns = ['_build']
master_doc = 'index'
source_suffix = ['.rst', '.md']
#source_parsers = {
#       '.md': CommonMarkParser,
#}
extensions = [
	'sphinx.ext.autodoc',
	'sphinx_rtd_theme',
	'sphinx_markdown_tables',
#	'recommonmark' 
]

from sphinx.highlighting import lexers
#from recommonmark.parser import CommonMarkParser
from pygments.lexers.web import PhpLexer
lexers['php'] = PhpLexer(startinline=True, linenos=1)
lexers['php-annotations'] = PhpLexer(startinline=True, linenos=1)
primary_domain = 'php'

# -- Options for HTML output -------------------------------------------------

htmlhelp_basename = 'secretariatdoc'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_path = ['_themes']

.. _Maria E. Adonay: https://amalgamaria.com/
