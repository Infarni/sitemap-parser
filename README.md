Script to download sitemap.xml. Its main purpose is to automatically download nested sitemaps as well.

# Instaliation dependies
run in shell
```sh
poetry install
```

# Run
To run use command:
```sh
poetry run python -m sitemap_parser.main https://some.url.com/sitemap.xml
```

# Files
Data from sitemap files saves in `data` dir
