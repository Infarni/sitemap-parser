import sys

from pathlib import Path

BASE_DIR: Path = Path(__file__).parent.parent
SITEMAP_DIR: Path = BASE_DIR.joinpath("data")

try:
    SITEMAP_URL: str = sys.argv[1]
except IndexError:
    print("Enter a url")
    sys.exit(1)
