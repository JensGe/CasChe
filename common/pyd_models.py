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

    logging_mode: int = 20
    crawling_speed_factor: float = 10
    default_crawl_delay: int = 5
    parallel_process: int = 12
    parallel_fetcher: int = 1

    iterations: int = 1
    fqdn_amount: int = 10
    url_amount: int = 0

    short_term_prio_mode: enum.SHORTPRIO = enum.SHORTPRIO.random
    long_term_prio_mode: enum.LONGPRIO = enum.LONGPRIO.random
    long_term_part_mode: enum.LONGPART = enum.LONGPART.none

    min_links_per_page: int = 1
    max_links_per_page: int = 1
    lpp_distribution_type: enum.PAGELINKDISTR = enum.PAGELINKDISTR.discrete

    internal_vs_external_threshold: float = 1.0
    new_vs_existing_threshold: float = 1.0


class CaseSettings(BaseModel):
    logging_mode: List[int] = None
    crawling_speed_factor: List[float] = None
    default_crawl_delay: List[int] = None
    parallel_process: List[int] = None
    parallel_fetcher: List[int] = None

    iterations: List[int] = None
    fqdn_amount: List[int] = None
    url_amount: List[int] = None

    short_term_prio_mode: List[enum.SHORTPRIO] = None
    long_term_prio_mode: List[enum.LONGPRIO] = None
    long_term_part_mode: List[enum.LONGPART] = None

    min_links_per_page: List[int] = None
    max_links_per_page: List[int] = None
    lpp_distribution_type: List[enum.PAGELINKDISTR] = None

    internal_vs_external_threshold: List[float] = None
    new_vs_existing_threshold: List[float] = None

