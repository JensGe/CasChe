import requests
from time import sleep

websch_database = "http://ec2-18-185-96-23.eu-central-1.compute.amazonaws.com/database/"
websch_settings = "http://ec2-18-185-96-23.eu-central-1.compute.amazonaws.com/settings/"
websch_stats = "http://ec2-18-185-96-23.eu-central-1.compute.amazonaws.com/stats/"


def delete_example_db():
    requests.delete(
        websch_database,
        json={
            "delete_url_refs": True,
            "delete_fetchers": True,
            "delete_urls": True,
            "delete_fqdns": True,
            "delete_reserved_fqdns": True,
        },
    )


def generate_example_db(
    fetcher: int = 0,
    fqdn_amount: int = 30,
    min_url_amount: int = 1,
    max_url_amount: int = 50,
    visited_ratio: float = 0.00,
    connection_amount: int = 0,
    fixed_crawl_delay: int = None,
):
    requests.post(
        websch_database,
        json={
            "fetcher_amount": fetcher,
            "fqdn_amount": fqdn_amount,
            "min_url_amount": min_url_amount,
            "max_url_amount": max_url_amount,
            "visited_ratio": visited_ratio,
            "connection_amount": connection_amount,
            "fixed_crawl_delay": fixed_crawl_delay,
        },
    )


def wait_for_example_db(settings):
    done = False
    first_run = True
    while not done:
        if first_run:
            sleep(5)
            first_run = False
        else:
            sleep(30)

        example_db = requests.get(websch_stats).json()

        fqdn_reached = example_db["frontier_amount"] == settings["fqdn_amount"]

        url_th = round(
            (settings["min_url_amount"] + settings["max_url_amount"])
            * settings["fqdn_amount"]
            / 2.15
        )
        url_reached = example_db["url_amount"] >= url_th

        hash_reached = example_db

        if fqdn_reached and url_reached:
            print(
                "** Threshold {} reached: url_amount={}".format(
                    url_th, example_db["url_amount"]
                )
            )
            done = True

        else:
            print(
                "** Threshold {} not reached: url_amount={}".format(
                    url_th, example_db["url_amount"]
                )
            )


def set_fetcher_settings(settings):
    requests.patch(
        websch_settings, json=settings,
    )
