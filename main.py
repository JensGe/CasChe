from systems import websch, database, compute, aws
from common import enum, pyd_models as pyd


case_settings = pyd.CaseSettings(
    logging_mode=None,
    crawling_speed_factor=None,
    default_crawl_delay=None,
    parallel_process=[1, 2, 4, 8, 16, 32, 64],
    iterations=[1],
    fqdn_amount=None,
    url_amount=None,
    long_term_mode=[enum.LTF.large_sites_first, enum.LTF.small_sites_first],
    short_term_mode=None,
    min_links_per_page=[1],
    max_links_per_page=[1],
    lpp_distribution_type=None,
    internal_vs_external_threshold=[1.0],
    new_vs_existing_threshold=[1.0]
)


def main():
    websch.delete_example_db()
    websch.generate_example_db(fqdn_amount=30, min_url_amount=5, max_url_amount=5)

    database.backup_table("fqdn_frontiers")
    database.backup_table("url_frontiers")

    settings_collection = compute.create_cases(case_settings)

    for setting in settings_collection:
        websch.delete_example_db()
        database.restore_table("fqdn_frontiers")
        database.restore_table("url_frontiers")
        websch.set_fetcher_settings(setting)

        aws.create_new_FetSim()



# ToDo
# [x] create db_example
#     [x] reset (request WebSch)
#     [x] generate example db
# [x] backup db_example
# [x] create all cases (FetcherSettings)
# [ ] for each FetcherSetting:
#     [x] restore db_example
#     [x] set current FetcherSetting
#     [ ] reboot / create FetSim Instance
#     [ ] download Log from S3 and name corresponding to FetcherSettings
# [ ] parse results



if __name__ == '__main__':
    main()
