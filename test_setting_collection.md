TEST COLLECTION
===============

# Parallel Processes
## Metrics

## Settings
```python
from common import enum
from common import pyd_models as pyd
from datetime import datetime

example_db_settings = dict(
    fqdn_amount=1000,
    min_url_amount=5,
    max_url_amount=5,
    fixed_crawl_delay=1,
)

project_settings = dict(
    name="parallel_processes",
    date=datetime.now().strftime("%Y-%m-%d"),
    repetition=1,
)

case_settings = pyd.CaseSettings(
    logging_mode=[20],
    crawling_speed_factor=[10.0],
    default_crawl_delay=[1],
    parallel_process=[i*2 for i in range(1,16)],
    parallel_fetcher=[1],
    iterations=[1],
    fqdn_amount=[i*4 for i in range(1,12)],
    url_amount=[0],
    long_term_part_mode=[enum.LONGPART.none],
    long_term_prio_mode=[enum.LONGPRIO.old_sites_first],
    short_term_prio_mode=[enum.SHORTPRIO.old_pages_first],
    min_links_per_page=[3],
    max_links_per_page=[3],
    lpp_distribution_type=[enum.PAGELINKDISTR.discrete],
    internal_vs_external_threshold=[1.0],
    new_vs_existing_threshold=[1.0],
)
```


# Parallel Fetcher
## Metrics

## Settings
```python
from common import enum
from common import pyd_models as pyd
from datetime import datetime

example_db_settings = dict(
    fqdn_amount=1000,
    min_url_amount=5,
    max_url_amount=5,
    fixed_crawl_delay=1,
)

project_settings = dict(
    name="parallel_fetchers",
    date=datetime.now().strftime("%Y-%m-%d"),
    repetition=5,
)

case_settings = pyd.CaseSettings(
    logging_mode=[20],
    crawling_speed_factor=[10.0],
    default_crawl_delay=[1],
    parallel_process=[12],
    parallel_fetcher=[i + 1 for i in range(30)],
    iterations=[1],
    fqdn_amount=[10],
    url_amount=[0],
    long_term_part_mode=[enum.LONGPART.none],
    long_term_prio_mode=[enum.LONGPRIO.old_sites_first],
    short_term_prio_mode=[enum.SHORTPRIO.old_pages_first],
    min_links_per_page=[3],
    max_links_per_page=[3],
    lpp_distribution_type=[enum.PAGELINKDISTR.discrete],
    internal_vs_external_threshold=[1.0],
    new_vs_existing_threshold=[1.0],
)
```


# Parallel Fetcher real test
## Metrics

## Settings
```python
from common import enum
from common import pyd_models as pyd
from datetime import datetime

example_db_settings = dict(
    fqdn_amount=5000,
    min_url_amount=5,
    max_url_amount=5,
    fixed_crawl_delay=10,
)

project_settings = dict(
    name="many_fetchers_real_fqdn_hash",
    date=datetime.now().strftime("%Y-%m-%d"),
    repetition=1,
)

case_settings = pyd.CaseSettings(
    logging_mode=[10],
    crawling_speed_factor=[10.0],
    default_crawl_delay=[10],
    parallel_process=[12],
    parallel_fetcher=[5],
    iterations=[10],
    fqdn_amount=[0],
    url_amount=[0],
    long_term_part_mode=[enum.LONGPART.fqdn_hash],
    long_term_prio_mode=[enum.LONGPRIO.old_sites_first],
    short_term_prio_mode=[enum.SHORTPRIO.old_pages_first],
    min_links_per_page=[3],
    max_links_per_page=[3],
    lpp_distribution_type=[enum.PAGELINKDISTR.discrete],
    internal_vs_external_threshold=[0.85],
    new_vs_existing_threshold=[0.35],
)

```


# 3. Large Sites vs Small Sites
## Metrics

## Settings
```python
from common import enum
from common import pyd_models as pyd
from datetime import datetime

example_db_settings = dict(
    fqdn_amount=5000,
    min_url_amount=5,
    max_url_amount=50,
)

project_settings = dict(
    name="large_vs_small",
    date=datetime.now().strftime("%Y-%m-%d"),
    repetition=10,
)

case_settings = pyd.CaseSettings(
    logging_mode=[20],
    crawling_speed_factor=[1.0],
    default_crawl_delay=[5],
    parallel_process=[15], #todo
    parallel_fetcher=[], #todo
    iterations=[10],
    fqdn_amount=[100],
    url_amount=[0],
    long_term_part_mode=[enum.LONGPART.none],
    long_term_prio_mode=[enum.LONGPRIO.large_sites_first, enum.LONGPRIO.small_sites_first, enum.LONGPRIO.random],
    short_term_prio_mode=[enum.SHORTPRIO.pagerank],
    min_links_per_page=[5],
    max_links_per_page=[5],
    lpp_distribution_type=[enum.PAGELINKDISTR.discrete],
    internal_vs_external_threshold=[1.0],
    new_vs_existing_threshold=[1.0],
)
```

# 4. old vs new Sites and Pages
## Metriken

## Settings
```python
from common import enum
from common import pyd_models as pyd
from datetime import datetime

example_db_settings = dict(
    fqdn_amount=5000,
    min_url_amount=5,
    max_url_amount=50,
)

project_settings = dict(
    name="old_vs_new",
    date=datetime.now().strftime("%Y-%m-%d"),
    repetition=10,
)

case_settings = pyd.CaseSettings(
    logging_mode=[20],
    crawling_speed_factor=[1.0],
    default_crawl_delay=[5],
    parallel_process=[15], #todo
    parallel_fetcher=[], #todo
    iterations=[10],
    fqdn_amount=[100],
    url_amount=[0],
    long_term_part_mode=[enum.LONGPART.none],
    long_term_prio_mode=[enum.LONGPRIO.old_sites_first, enum.LONGPRIO.new_sites_first, enum.LONGPRIO.random],
    short_term_prio_mode=[enum.SHORTPRIO.old_pages_first, enum.SHORTPRIO.new_pages_first, enum.SHORTPRIO.random],
    min_links_per_page=[5],
    max_links_per_page=[5],
    lpp_distribution_type=[enum.PAGELINKDISTR.discrete],
    internal_vs_external_threshold=[1.0],
    new_vs_existing_threshold=[1.0],
)
```

# Partitionierung TLD vs. FQDN Hash vs. CH

Web Crawler Metrik: Durchsatz