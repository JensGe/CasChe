
# 1. Parallel Process Test
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
    repetition=5,
)

case_settings = pyd.CaseSettings(
    logging_mode=[20],
    crawling_speed_factor=[10.0],
    default_crawl_delay=[1],
    parallel_process=[i + 1 for i in range(30)],
    parallel_fetcher=[1],
    iterations=[1],
    fqdn_amount=[10],
    url_amount=[0],
    long_term_mode=[enum.LTF.old_sites_first],
    short_term_mode=[enum.STF.old_pages_first],
    min_links_per_page=[3],
    max_links_per_page=[3],
    lpp_distribution_type=[enum.LPPDISTR.discrete],
    internal_vs_external_threshold=[1.0],
    new_vs_existing_threshold=[1.0],
)
```


# 2. Parallel Fetcher
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
    parallel_process=[16], #todo
    parallel_fetcher=[i + 1 for i in range(30)],
    iterations=[1],
    fqdn_amount=[10],
    url_amount=[0],
    long_term_mode=[enum.LTF.old_sites_first],
    short_term_mode=[enum.STF.old_pages_first],
    min_links_per_page=[3],
    max_links_per_page=[3],
    lpp_distribution_type=[enum.LPPDISTR.discrete],
    internal_vs_external_threshold=[1.0],
    new_vs_existing_threshold=[1.0],
)
```


# 3. Large Sites vs Small Sites
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
    long_term_mode=[enum.LTF.large_sites_first, enum.LTF.small_sites_first, enum.LTF.random],
    short_term_mode=[enum.STF.pagerank],
    min_links_per_page=[5],
    max_links_per_page=[5],
    lpp_distribution_type=[enum.LPPDISTR.discrete],
    internal_vs_external_threshold=[1.0],
    new_vs_existing_threshold=[1.0],
)
```

4. old vs new Sites and Pages
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
    long_term_mode=[enum.LTF.old_sites_first, enum.LTF.new_sites_first, enum.LTF.random],
    short_term_mode=[enum.STF.old_pages_first, enum.STF.new_pages_first, enum.STF.random],
    min_links_per_page=[5],
    max_links_per_page=[5],
    lpp_distribution_type=[enum.LPPDISTR.discrete],
    internal_vs_external_threshold=[1.0],
    new_vs_existing_threshold=[1.0],
)
```