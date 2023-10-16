# Configuration file for the Sphinx documentation builder.
#
# Options for this theme, pydata:
# https://pydata-sphinx-theme.readthedocs.io/en/stable/
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "oawiki"
copyright = "2023, The OAWiki Team"
author = "The OAWiki Team"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Turn all bad references into warnings
nitpicky = True

extensions = ["myst_parser", "sphinx_design", "sphinx_togglebutton"]

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
    "myst.strikethrough",
]

html_theme = "pydata_sphinx_theme"

# by default, this has more, but we value brevity.
html_theme_options = {
    "footer_start": ["copyright"],
    "footer_end": ["sphinx-version"],
    "secondary_sidebar_items": ["page-toc", "edit-this-page"],
    "logo": {"text": "OAWiki"},
    "use_edit_page_button": True,
}

html_context = {
    "github_url": "https://github.com",
    "github_user": "observational-dev",
    "github_repo": "oawiki",
    "github_version": "main",
    "doc_path": "src/",
}

html_static_path = ["_static"]


def setup(app):
    # Styles applied to the entire wiki
    app.add_css_file("css/custom.css")
