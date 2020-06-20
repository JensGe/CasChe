from datetime import datetime
from common import pyd_models as pyd
from common import enum

# 1. Parallel Process Test
example_db_settings = dict(
    fqdn_amount=1000,
    min_url_amount=5,
    max_url_amount=5,
)

project_settings = dict(
    name="parallel_processes",
    date=datetime.now().strftime("%Y-%m-%d"),
    repetition=5,
)

case_settings = pyd.CaseSettings(
    logging_mode=[20],
    crawling_speed_factor=[1.0],
    default_crawl_delay=[5],
    parallel_process=[i + 1 for i in range(30)],
    parallel_fetcher=[1],
    iterations=[1],
    fqdn_amount=[50],
    url_amount=[0],
    long_term_mode=[enum.LTF.old_sites_first],
    short_term_mode=[enum.STF.old_pages_first],
    min_links_per_page=[5],
    max_links_per_page=[5],
    lpp_distribution_type=[enum.LPPDISTR.discrete],
    internal_vs_external_threshold=[1.0],
    new_vs_existing_threshold=[1.0],
)

# 2. Parallel Fetcher
example_db_settings = dict(
    fqdn_amount=1000,
    min_url_amount=5,
    max_url_amount=5,
)

project_settings = dict(
    name="parallel_processes",
    date=datetime.now().strftime("%Y-%m-%d"),
    repetition=5,
)

case_settings = pyd.CaseSettings(
    logging_mode=[20],
    crawling_speed_factor=[1.0],
    default_crawl_delay=[5],
    parallel_process=[16],
    parallel_fetcher=[1, 2, 4, 8, 16],
    iterations=[1],
    fqdn_amount=[50],
    url_amount=[0],
    long_term_mode=[enum.LTF.old_sites_first],
    short_term_mode=[enum.STF.old_pages_first],
    min_links_per_page=[5],
    max_links_per_page=[5],
    lpp_distribution_type=[enum.LPPDISTR.discrete],
    internal_vs_external_threshold=[1.0],
    new_vs_existing_threshold=[1.0],
)
