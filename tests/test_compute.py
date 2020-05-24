from systems import compute
from common import enum, pyd_models as pyd
import os

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


def test_create_repetition_cases():
    cases = pyd.CaseSettings(
        parallel_process=[1, 2],
        default_crawl_delay=[1],
    )
    repetition = 3

    s_coll = compute.create_cases(cases, repetition)

    assert len(s_coll) == 6

    assert s_coll == [
        {
            "parallel_process": 1,
            "default_crawl_delay": 1,
        },
        {
            "parallel_process": 1,
            "default_crawl_delay": 1,
        },
        {
            "parallel_process": 1,
            "default_crawl_delay": 1,
        },
        {
            "parallel_process": 2,
            "default_crawl_delay": 1,
        },
        {
            "parallel_process": 2,
            "default_crawl_delay": 1,
        },
        {
            "parallel_process": 2,
            "default_crawl_delay": 1,
        },
    ]



def test_parse_results():
    results = compute.jsonify_results()
    print(results)

    assert len(results) > 0


def test_get_fetcher_settings():
    row_1 = "2020-05-22 00:12:34.701 root INFO Fetcher Settings: {'logging_mode': 20, 'crawling_speed_factor': 10.0, 'default_crawl_delay': 10, 'parallel_process': 2, 'iterations': 1, 'fqdn_amount': 10, 'url_amount': 0, 'min_links_per_page': 2, 'max_links_per_page': 2, 'lpp_distribution_type': 'discrete', 'internal_vs_external_threshold': 1.0, 'new_vs_existing_threshold': 1.0, 'long_term_mode': 'small_sites_first', 'short_term_mode': 'random'}"
    row_2 = "2020-05-22 00:12:34.70 root INFO Fetcher Settings: {'logging_mode': 20, 'crawling_speed_factor': 10.0, 'default_crawl_delay': 10, 'parallel_process': 2, 'iterations': 1, 'fqdn_amount': 10, 'url_amount': 0, 'min_links_per_page': 2, 'max_links_per_page': 2, 'lpp_distribution_type': 'discrete', 'internal_vs_external_threshold': 1.0, 'new_vs_existing_threshold': 1.0, 'long_term_mode': 'small_sites_first', 'short_term_mode': 'random'}"

    fetcher_settings1 = compute.get_fetcher_settings(row_1)
    fetcher_settings2 = compute.get_fetcher_settings(row_2)
    asserted_fs = dict(
        logging_mode=20,
        crawling_speed_factor=10.0,
        default_crawl_delay=10,
        parallel_process=2,
        iterations=1,
        fqdn_amount=10,
        url_amount=0,
        min_links_per_page=2,
        max_links_per_page=2,
        lpp_distribution_type="discrete",
        internal_vs_external_threshold=1.0,
        new_vs_existing_threshold=1.0,
        long_term_mode="small_sites_first",
        short_term_mode="random",
    )

    assert fetcher_settings1 == asserted_fs
    assert fetcher_settings2 == asserted_fs


def test_get_iteration_results():
    row_1 = "2020-05-22 00:14:28.190 root INFO Iteration Stats: load (59.47 ms), fetch (22.58 s), fetch_cpu (0.757 s), submit (18.185 ms)."
    row_2 = "2020-05-22 00:14:28.19 root INFO Iteration Stats: load (59.47 ms), fetch (22.58 s), fetch_cpu (0.757 s), submit (18.185 ms)."

    iteration_results1 = compute.get_iteration_results(row_1)
    iteration_results2 = compute.get_iteration_results(row_2)

    asserted_results = dict(
        load="59.47 ms", fetch="22.58 s", fetch_cpu="0.757 s", submit="18.185 ms",
    )

    assert iteration_results1 == asserted_results
    assert iteration_results2 == asserted_results


def test_get_stats_results():
    row = "2020-05-22 00:14:28.19 root INFO DB Stats: frontier_amount: 1005, url_amount: 5230"

    stats_results = compute.get_stats_results(row)

    asserted_results = dict(frontier_amount=1005, url_amount=5230)

    assert stats_results == asserted_results


def test_archive_project():
    if not os.path.exists("fetsim-logs"):
        os.makedirs("fetsim-logs")

    with open("fetsim-logs/file1.txt", "w") as file1:
        file1.write("content1")
    with open("fetsim-logs/file2.txt", "w") as file2:
        file2.write("content2")

    compute.archive_project("fetsim-logs_test_2020-05-24")

