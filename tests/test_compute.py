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

    iteration_results1 = compute.get_stats_results(row_1)
    iteration_results2 = compute.get_stats_results(row_2)

    asserted_results = dict(
        load="59.47 ms", fetch="22.58 s", fetch_cpu="0.757 s", submit="18.185 ms",
    )

    assert iteration_results1 == asserted_results
    assert iteration_results2 == asserted_results


def test_get_stats_results_db():
    row = "2020-05-22 00:14:28.19 root INFO DB Stats: db_frontier_amount: 1005, db_url_amount: 5230\n"

    stats_results = compute.get_db_stats_results(row)

    asserted_results = dict(
        db_access_time="2020-05-22 00:14:28.19",
        db_frontier_amount="1005",
        db_url_amount="5230",
    )

    assert stats_results == asserted_results


def test_get_stats_results_iter():
    row = "2020-07-11 19:40:39,001 FETSIM INFO Iteration Stats: iter_load_duration: 72.304, iter_fetch_start: 2020-07-11 19:40:37.437, iter_fetch_duration: 1.023, iter_fetch_cpu_time: 0.369, iter_submit_duration: 35.696\n"

    stats_results = compute.get_db_stats_results(row)

    asserted_results = dict(
        iter_load_duration="72.304",
        iter_fetch_start="2020-07-11 19:40:37.437",
        iter_fetch_duration="1.023",
        iter_fetch_cpu_time="0.369",
        iter_submit_duration="35.696",
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
2020-07-11 19:40:37,869 FETSIM INFO Fetcher Settings: {'logging_mode': 20, 'crawling_speed_factor': 10.0, 'default_crawl_delay': 10, 'parallel_process': 1, 'parallel_fetcher': 1, 'iterations': 1, 'fqdn_amount': 1, 'url_amount': 0, 'short_term_prio_mode': 'random', 'long_term_prio_mode': 'random', 'long_term_part_mode': 'none', 'min_links_per_page': 1, 'max_links_per_page': 1, 'lpp_distribution_type': 'discrete', 'internal_vs_external_threshold': 1.0, 'new_vs_existing_threshold': 1.0}
2020-07-11 19:40:37,942 FETSIM INFO Frontier Stats: 1 FQDNs, 1 URLs
2020-07-11 19:40:38,961 FETSIM INFO Short Term Frontier processed. FQDN www.s1umjmr3mogop.za, URLs 1
2020-07-11 19:40:38,965 FETSIM INFO Response Stats: 1 FQDNs, 2 URLs
2020-07-11 19:40:39,001 FETSIM INFO Iteration Stats: iter_load_duration: 72.304, iter_fetch_start: 2020-07-11 19:40:37.437, iter_fetch_duration: 1.023, iter_fetch_cpu_time: 0.369, iter_submit_duration: 35.696.
2020-07-11 19:40:44,096 FETSIM INFO DB Stats: db_frontier_amount: 600, db_url_amount: 802, db_avg_freshness: 2017-08-16 19:58:14.213443, db_visited_ratio: 0.19201995012468828, db_fqdn_hash_range: 0.34
2020-07-11 19:40:44,148 FETSIM INFO uploading...
2020-07-11 19:40:44,467 FETSIM INFO Terminating Program
        """
        )

    results = compute.jsonify_results()
    print(results)
    assert len(results) == 1
