import requests

from sitemap_parser import config, constants, sitemap


def main() -> None:
    session: requests.Session = requests.Session()
    session.headers = {"User-agent": constants.USER_AGENT}
    sitemap.parse(session, config.SITEMAP_URL)


if __name__ == "__main__":
    main()
