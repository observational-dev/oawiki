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
