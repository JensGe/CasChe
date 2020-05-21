from systems import compute
from common import enum, pyd_models as pyd


def test_create_cases():

    cases = pyd.CaseSettings(
        parallel_process=[1, 2, 4],
        long_term_mode=[enum.LTF.small_sites_first, enum.LTF.large_sites_first],
        default_crawl_delay=[1],
    )

    s_coll = compute.create_cases(cases)

    assert isinstance(s_coll, list)
    assert len(s_coll) == 6
    assert s_coll == [
        {
            "default_crawl_delay": 1,
            "parallel_process": 1,
            "long_term_mode": "small_sites_first",
        },
        {
            "default_crawl_delay": 1,
            "parallel_process": 1,
            "long_term_mode": "large_sites_first",
        },
        {
            "default_crawl_delay": 1,
            "parallel_process": 2,
            "long_term_mode": "small_sites_first",
        },
        {
            "default_crawl_delay": 1,
            "parallel_process": 2,
            "long_term_mode": "large_sites_first",
        },
        {
            "default_crawl_delay": 1,
            "parallel_process": 4,
            "long_term_mode": "small_sites_first",
        },
        {
            "default_crawl_delay": 1,
            "parallel_process": 4,
            "long_term_mode": "large_sites_first",
        },
    ]
