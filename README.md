# :sparkles: Welcome to the OAWiki Repository! :telescope:

This is the repository for the OAWiki website.

## Contributing

### Building the site

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
