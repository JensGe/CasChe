from systems import websch
from common import pyd_models as pyd


def test_set_fetcher_settings():
    settings = {"default_crawl_delay": 1, "parallel_process": 1, "iterations": 1}
    websch.set_fetcher_settings(settings)
