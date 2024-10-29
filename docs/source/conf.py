# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath('../../src/HAlphaAnomalyzer'))

project = 'HAlphaAnomalyzer'
copyright = '2024, Mahsa Khazaei, Heba Mahdi, Azim Ahmadzadeh'
author = 'Mahsa Khazaei, Heba Mahdi, Azim Ahmadzadeh'
# release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode', 'sphinx.ext.autosummary', 'sphinx.ext.doctest', 'autoapi.extension', 'myst_parser']
autoapi_dirs = ['../../src/HAlphaAnomalyzer/']

autosummary_generate = True

templates_path = ['_templates']
exclude_patterns = []

# To serve custome html files
#html_extra_path = ['_static']
#master_doc = 'index'



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
