from pydantic import BaseModel
from common import enum
from typing import List


class ExampleDBSettings(BaseModel):
    crawler_amount: int = 0
    fixed_crawl_delay: int = None
    fqdn_amount: int = 20
    min_url_amount: int = 5
    max_url_amount: int = 5
    visited_ratio: float = 0.0
    connection_amount: int = 0


class FetcherSettings(BaseModel):
    logging_mode: int = 20  # 10: DEBUG, 20: INFO
    crawling_speed_factor: float = 10.0
    default_crawl_delay: int = 10
    parallel_process: int = 10
    parallel_fetcher: int = 1

    iterations: int = 10
    fqdn_amount: int = 30
    url_amount: int = 0  # unlimited

    long_term_mode = enum.LTF.random
    short_term_mode = enum.STF.random

    min_links_per_page: int = 2  # Check Literature
    max_links_per_page: int = 5
    lpp_distribution_type: enum.LPPDISTR = enum.LPPDISTR.discrete

    internal_vs_external_threshold: float = 0.85  # Check Literature
    new_vs_existing_threshold: float = 0.35


class CaseSettings(BaseModel):
    logging_mode: List[int] = None
    crawling_speed_factor: List[float] = None
    default_crawl_delay: List[int] = None
    parallel_process: List[int] = None
    parallel_fetcher: List[int] = None

    iterations: List[int] = None
    fqdn_amount: List[int] = None
    url_amount: List[int] = None

    long_term_mode: List[enum.LTF] = None
    short_term_mode: List[enum.STF] = None

    min_links_per_page: List[int] = None  # Check Literature
    max_links_per_page: List[int] = None
    lpp_distribution_type: List[enum.LPPDISTR] = None

    internal_vs_external_threshold: List[float] = None
    new_vs_existing_threshold: List[float] = None

