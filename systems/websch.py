import requests
from common import pyd_models as pyd

websch_database = "http://ec2-18-185-96-23.eu-central-1.compute.amazonaws.com/database/"
websch_settings = "http://ec2-18-185-96-23.eu-central-1.compute.amazonaws.com/settings/"


def delete_example_db():
    requests.delete(
        websch_database,
        json={
            "delete_url_refs": True,
            "delete_crawlers": True,
            "delete_urls": True,
            "delete_fqdns": True,
            "delete_reserved_fqdns": True,
        },
    )


def generate_example_db(
    crawler_amount: int = 0,
    fqdn_amount: int = 30,
    min_url_amount: int = 1,
    max_url_amount: int = 50,
    visited_ratio: float = 0.00,
    connection_amount: int = 0,
):
    requests.post(
        websch_database,
        json={
            "crawler_amount": crawler_amount,
            "fqdn_amount": fqdn_amount,
            "min_url_amount": min_url_amount,
            "max_url_amount": max_url_amount,
            "visited_ratio": visited_ratio,
            "connection_amount": connection_amount,
        },
    )


def set_fetcher_settings(settings):
    # current_setting = pyd.FetcherSettings(**settings)
    requests.patch(
        websch_settings,
        json=settings,
    )