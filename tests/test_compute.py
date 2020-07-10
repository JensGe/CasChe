from systems import compute
from common import enum, pyd_models as pyd
from datetime import datetime
import os


def test_create_cases():

    project_settings = dict(
        name="test_test",
        date=datetime.now().strftime("%Y-%m-%d"),
        repetition=1,
        parallel_fetcher=1,
    )

    cases = pyd.CaseSettings(
        parallel_process=[1, 2, 4],
        long_term_prio_mode=[
            enum.LONGPRIO.small_sites_first,
            enum.LONGPRIO.large_sites_first,
        ],
        default_crawl_delay=[1],
    )

    s_coll = compute.create_cases(cases, project_settings)

    assert isinstance(s_coll, list)
    assert len(s_coll) == 6
    assert s_coll == [
        {
            "default_crawl_delay": 1,
            "parallel_process": 1,
            "long_term_prio_mode": "small_sites_first",
        },
        {
            "default_crawl_delay": 1,
            "parallel_process": 1,
            "long_term_prio_mode": "large_sites_first",
        },
        {
            "default_crawl_delay": 1,
            "parallel_process": 2,
            "long_term_prio_mode": "small_sites_first",
        },
        {
            "default_crawl_delay": 1,
            "parallel_process": 2,
            "long_term_prio_mode": "large_sites_first",
        },
        {
            "default_crawl_delay": 1,
            "parallel_process": 4,
            "long_term_prio_mode": "small_sites_first",
        },
        {
            "default_crawl_delay": 1,
            "parallel_process": 4,
            "long_term_prio_mode": "large_sites_first",
        },
    ]


def test_create_repetition_cases():
    cases = pyd.CaseSettings(parallel_process=[1, 2], default_crawl_delay=[1],)
    project_settings = dict(
        name="test_test",
        date=datetime.now().strftime("%Y-%m-%d"),
        repetition=3,
        parallel_fetcher=1,
    )

    s_coll = compute.create_cases(cases, project_settings)

    assert len(s_coll) == 6

    assert s_coll == [
        {"parallel_process": 1, "default_crawl_delay": 1,},
        {"parallel_process": 1, "default_crawl_delay": 1,},
        {"parallel_process": 1, "default_crawl_delay": 1,},
        {"parallel_process": 2, "default_crawl_delay": 1,},
        {"parallel_process": 2, "default_crawl_delay": 1,},
        {"parallel_process": 2, "default_crawl_delay": 1,},
    ]


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
    row = "2020-05-22 00:14:28.19 root INFO DB Stats: db_frontier_amount: 1005, db_url_amount: 5230\n"

    stats_results = compute.get_stats_results(row)

    asserted_results = dict(
        db_access_time="2020-05-22 00:14:28.19",
        db_frontier_amount="1005",
        db_url_amount="5230",
    )

    assert stats_results == asserted_results


def test_archive_project():
    if not os.path.exists("fetsim-logs"):
        os.makedirs("fetsim-logs")

    project_settings = dict(
        name="test_test",
        date=datetime.now().strftime("%Y-%m-%d"),
        repetition=1,
        parallel_fetcher=1,
    )

    with open("fetsim-logs/file1.log", "w") as file1:
        file1.write("content1")
    with open("fetsim-logs/file2.log", "w") as file2:
        file2.write("content2")

    compute.archive_project(project_settings)


def test_multiple_iteration_results():
    if not os.path.exists("fetsim-logs"):
        os.makedirs("fetsim-logs")

    with open("fetsim-logs/file1.log", "w") as file1:
        file1.write(
            """
2020-06-23 10:56:19.585 root INFO Fetcher Settings: {'logging_mode': 20, 'crawling_speed_factor': 10.0, 'default_crawl_delay': 10, 'parallel_process': 12, 'parallel_fetcher': 5, 'iterations': 5, 'fqdn_amount': 10, 'url_amount': 0, 'long_term_mode': 'fqdn_hash', 'short_term_mode': 'old_pages_first', 'min_links_per_page': 3, 'max_links_per_page': 3, 'lpp_distribution_type': 'discrete', 'internal_vs_external_threshold': 0.85, 'new_vs_existing_threshold': 0.35}
2020-06-23 10:56:19.623 root INFO Frontier Stats: 0 FQDNs, 0 URLs
2020-06-23 10:56:19.717 root INFO Response Stats: 0 FQDNs, 0 URLs
2020-06-23 10:56:19.725 root INFO Iteration Stats: load (38.244 ms), fetch (0.093 s), fetch_cpu (0.897 s), submit (8.064 ms).
2020-06-23 10:56:40.457 root INFO DB Stats: frontier_amount: 1042, url_amount: 5218, avg_freshness: 2020-06-23 10:56:23.233600, visited_ratio: 0.038328861632809505
2020-06-23 10:56:19.758 root INFO Frontier Stats: 0 FQDNs, 0 URLs
2020-06-23 10:56:19.853 root INFO Response Stats: 0 FQDNs, 0 URLs
2020-06-23 10:56:19.861 root INFO Iteration Stats: load (32.092 ms), fetch (0.095 s), fetch_cpu (0.968 s), submit (7.377 ms).
2020-06-23 10:56:40.457 root INFO DB Stats: frontier_amount: 1042, url_amount: 5218, avg_freshness: 2020-06-23 10:56:23.233600, visited_ratio: 0.038328861632809505
2020-06-23 10:56:19.895 root INFO Frontier Stats: 0 FQDNs, 0 URLs
2020-06-23 10:56:19.983 root INFO Response Stats: 0 FQDNs, 0 URLs
2020-06-23 10:56:19.990 root INFO Iteration Stats: load (33.396 ms), fetch (0.087 s), fetch_cpu (1.048 s), submit (6.756 ms).
2020-06-23 10:56:40.457 root INFO DB Stats: frontier_amount: 1042, url_amount: 5218, avg_freshness: 2020-06-23 10:56:23.233600, visited_ratio: 0.038328861632809505
2020-06-23 10:56:20.78 root INFO Frontier Stats: 0 FQDNs, 0 URLs
2020-06-23 10:56:20.184 root INFO Response Stats: 0 FQDNs, 0 URLs
2020-06-23 10:56:20.192 root INFO Iteration Stats: load (88.091 ms), fetch (0.106 s), fetch_cpu (1.129 s), submit (6.707 ms).
2020-06-23 10:56:40.457 root INFO DB Stats: frontier_amount: 1042, url_amount: 5218, avg_freshness: 2020-06-23 10:56:23.233600, visited_ratio: 0.038328861632809505
2020-06-23 10:56:20.228 root INFO Frontier Stats: 0 FQDNs, 0 URLs
2020-06-23 10:56:20.378 root INFO Response Stats: 0 FQDNs, 0 URLs
2020-06-23 10:56:20.386 root INFO Iteration Stats: load (36.013 ms), fetch (0.149 s), fetch_cpu (1.215 s), submit (7.14 ms).
2020-06-23 10:56:40.457 root INFO DB Stats: frontier_amount: 1042, url_amount: 5218, avg_freshness: 2020-06-23 10:56:23.233600, visited_ratio: 0.038328861632809505
2020-06-23 10:56:40.685 root INFO Upload: i-0484db4715db2d984.log
        """
        )

    results = compute.jsonify_results()
    print(results)
    assert len(results) == 5
