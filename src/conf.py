import pathlib
from collections import defaultdict

import git
import pandas as pd

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

extensions = [
    "myst_parser",
    "sphinx_design",
    "notfound.extension",
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
    "myst.strikethrough",
]

html_theme = "pydata_sphinx_theme"

# by default, this has more, but we value brevity.
html_theme_options = {
    "footer_start": ["copyright"],
    "footer_end": ["sphinx-version"],
    "secondary_sidebar_items": ["page-toc", "edit-this-page", "git-history"],
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

notfound_urls_prefix = ''


def add_context_funcs(app, pagename, templatename, context, doctree):
    repo_url = "https://github.com/observational-dev/oawiki"
    repo = git.Repo(pathlib.Path(__file__).parents[1])

    def add_git_history() -> str:
        """Generate the git history content for each page.

        Returns
        -------
        str
            Git history rendered as HTML.
        """
        if "page_source_suffix" in context:
            filename = (pathlib.Path(__file__).parent / pagename).with_suffix(
                context["page_source_suffix"]
            )
            commit_log = defaultdict(list)
            for commit in repo.iter_commits(paths=filename):
                commit_log["Date"].append(
                    f'<a href="{repo_url}/commit/{commit.hexsha}">'
                    f"{str(commit.authored_datetime)}</a>"
                )
                commit_log["Author"].append(commit.author.name)
                commit_log["Message"].append(commit.summary)
            return (
                pd.DataFrame(commit_log)
                .sort_values("Date")
                .to_html(
                    index=False,
                    escape=False,
                    classes="git-history",
                    justify="center",
                )
            )
        return ""

    context["add_git_history"] = add_git_history


def setup(app):
    # Styles applied to the entire wiki
    app.add_css_file("css/custom.css")
    app.add_js_file("js/custom.js")

    app.connect("html-page-context", add_context_funcs)
