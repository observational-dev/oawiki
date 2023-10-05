# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'oawiki'
copyright = '2023, The OAWiki Team'
author = 'The OAWiki Team'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Turn all bad references into warnings
nitpicky = True

extensions = [
    'myst_parser',
    'sphinx_design',
]

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    # "replacements",
    "smartquotes",
    "strikethrough",
    # "substitution",
    "tasklist",
]

suppress_warnings = [
    'myst.strikethrough',
]

html_theme = "pydata_sphinx_theme"
html_static_path = ['_static']