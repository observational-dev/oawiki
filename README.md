# :sparkles: Welcome to the OAWiki Repository! :telescope:

Welcome to the source for the OAWiki - https://wiki.observational.space ! If you are interested in contributing an article, thank you! The next two sections are just for you :)

## Contributing - Authoring

The wiki pages are written in markdown. You might be familiar with it - `**bold**` and `# heading` and `[link text](url)` (for more, check out [here](https://commonmark.org/help/)). You can write markdown text anywhere; if you would like a suggestion that isn't here on GitHub, try https://hackmd.io

Some considerations as you write:

- acceptable content: keep it professional.
- proper attribution: many astrophotography images take tens or even a hundred hours to create. Proper attribution and permission is very important.
- license notice: the wiki (and thus any content you contribute) is under CC-BY-SA-4.0 which is common for educational material (and very similar to that of Wikipedia).

## Contributing - Adding your Contribution

### The Fast Way

The easiest way is to send your article or contribution in the discord, and ask a wiki maintainer to integrate it. This is recommended for first time contributors.

### The DIY Way

You can also do that integration process yourself. At this GitHub, you'll open a pull request with your change, which will be approved by a maintainer and automatically made live on the site. You'll need to make an account on GitHub for this. Specifically, the process goes:

- on the wiki page you wish to change, on the right sidebar, click `Edit on GitHub`
- make your changes (tip: just above the top left of the editor area, there's a edit / preview switch. Remember this isn't a perfect preview but it's sometimes helpful)
- near the top right is a big green `Commit changes...` to click when you're satisfied
- The `Commit message` is important; extended description etc is not. The commit message is what will be shown when folks look through a page's history, so replace the default and just breifly describe what was changed, and put your name in parentheses afterward. You don't need to say the file / page name here.
  - example: "wrote base article (yourname)" or "added section for jabberwalk tips (yourname)" or "fixed inaccuracy about Vorpal Blades (yourname)"
- Click the big green buttons it guides you through - fork the repo, create a branch
- now near the upper left corner of the page, click the `Pull requests` tab, and hopefully there's a yellow box saying there is recent activity and suggesting you `Compare & pull request` - do that, then click the next big green button `Create pull request`
- Your part is now done! Wiki maintainers will take a gander and approve it, and then it becomes live on the website! Thank you!

## Building the Wiki Locally (optional)

For the nerds, here's how!

### Setup

The site is built from markdown using
[`sphinx`](https://github.com/sphinx-doc/sphinx). To build the site, you'll
first need to install python via your favorite method. Then install the
python dependencies:

```bash
pip install -r requirements.txt
```

Inside `src/` you'll find a `Makefile` which helps orchestrate the build.
Simply type

```bash
make html
```

to build the site; the output will be written to `src/_build/html/`. Using your
browser, open `src/_build/html/index.html` to view the site.

### Pre-commit hooks

[`pre-commit`](https://pre-commit.com/) is a python tool which allows for
formatting and linting tools to be run automatically when a `git commit` is
called. Here, we use it to automatically

- Remove whitespace at the end of lines
- Put a newline at the end of every file, if there isn't one there already
- Check that yaml, json, and python files are valid
- Check that we don't accidentally add huge files to the repo
- Sort entries in `requirements.txt`
- Replace mixed line endings (`\r\n` -> `\n`)
- Format pretty much all the files in the repo
- Perform static analysis on python types
- Sort python imports
- Lint javascript code

To enable these hooks, make sure the dependencies are installed:

```bash
pip install -r requirements.txt
```

Then install the hooks:

```bash
pre-commit install
```

Now, any time you do `git commit`, these checks will be automatically run. If
`pre-commit` modifies your code, it will tell you that it automatically modified
your code. If you `git add` those modified files and then call `git commit`
again, the checks will run again. Once all the checks are passing, you'll be
able to commit as normal.

If you temporarily want to disable the pre-commit hooks, you can do `git commit
-n` to disable the hooks for just that commit.
