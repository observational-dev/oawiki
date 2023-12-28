import logging
import pathlib
from collections import defaultdict

import git
import pandas as pd

logger = logging.getLogger(__name__)

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

notfound_urls_prefix = ""


def run_once(f):
    """Decorator which ensures the decorate function only runs once.

    If the function has already run once, None is returned.
    """

    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)

    wrapper.has_run = False
    return wrapper


static_dir = pathlib.Path(__file__).parent / "_static"


@run_once
def generate_eyepieces_json(path: str | pathlib.Path | None = None):
    """Generate a JSON blob containing eyepiece data from the buyer's guide to eyepieces.

    Parameters
    ----------
    path : str | pathlib.Path | None
        Path to the buyer's guide to eyepieces excel spreadsheet. If None, a default
        spreadsheet is loaded from the src/visual/eyepieces/ directory.
    """
    if path is None:
        path = (
            pathlib.Path(__file__).parent
            / "visual"
            / "eyepieces"
            / "2023_buyers_guide_to_eyepieces.xlsx"
        )
    elif isinstance(path, str):
        path = pathlib.Path(path)

    path_fixed = static_dir / "eyepiece_buyers_guide_fixed.json"
    path_zoom = static_dir / "eyepiece_buyers_guide_zoom.json"

    path_fixed.unlink(missing_ok=True)
    path_zoom.unlink(missing_ok=True)

    pd.read_excel(
        path,
        sheet_name="Eyepieces",
        skiprows=4,
        usecols="A:O",
        na_values="?",
    ).to_json(path_fixed, orient="records")
    pd.read_excel(
        path,
        sheet_name="Zooms",
    ).to_json(path_zoom, orient="records")


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
            commits = list(repo.iter_commits(paths=filename))
            if commits:
                for commit in commits:
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
            else:
                logger.warning(
                    f"{pagename} has no commit history; skipping page history "
                    "generation. Has it been committed yet?"
                )

        return ""

    context["add_git_history"] = add_git_history


def add_per_page_assets(app, pagename, templatename, context, doctree):
    if pagename == "index":
        app.add_css_file("css/splash.css")
        return "splash.html"
    elif pagename == "visual/eyepieces/ernests_list":
        app.add_js_file("js/visual/eyepieces/ernests_list.js", loading_method="defer")
        app.add_css_file("css/visual/eyepieces/ernests_list.css")
        return "ernests_list.html"
    elif pagename == "visual/eyepieces/calculators":
        app.add_css_file("css/visual/eyepieces/calculators.css")
        app.add_js_file("https://d3js.org/d3.v6.js")
        app.add_js_file("js/visual/eyepieces/calculators.js", loading_method="defer")
        return "eyepiece_calculators.html"


# Pregenerate the json files containing the eyepieces data
generate_eyepieces_json()


def setup(app):
    # Styles applied to the entire wiki
    app.add_css_file("css/custom.css")
    app.add_js_file("js/custom.js")

    app.add_css_file("css/tabulator_styles.css")
    app.add_js_file("https://unpkg.com/tabulator-tables/dist/js/tabulator.min.js")

    app.connect("html-page-context", add_context_funcs)
    app.connect("html-page-context", add_per_page_assets)
