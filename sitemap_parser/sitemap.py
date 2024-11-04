import pathlib
import requests

from bs4 import BeautifulSoup
from loguru import logger

from sitemap_parser import config


def parse(
    session: requests.Session, url: str, parent: pathlib.Path | None = None
) -> None:
    response: requests.Response = session.get(url)

    soup: BeautifulSoup = BeautifulSoup(response.content, "lxml-xml")
    items = soup.find_all("loc")

    for item in items:
        logger.info(item.text)
        if item.text[-4:] == ".xml":
            logger.info("Has inner sitemap")
            name: str = item.text.split("/")[-1][:-4]
            if parent:
                dir: pathlib.Path = parent.joinpath(name)
            else:
                dir = config.SITEMAP_DIR.joinpath(name)

            parse(session, item.text, dir)

    if not (parent is None):
        parent.parent.mkdir(parents=True, exist_ok=True)
        path = pathlib.Path(str(parent) + ".xml")
    else:
        config.SITEMAP_DIR.mkdir(parents=True, exist_ok=True)
        path = config.SITEMAP_DIR.joinpath("sitemap.xml")

    with open(path, "w") as file:
        logger.info("Writing...")
        file.write(soup.prettify())
