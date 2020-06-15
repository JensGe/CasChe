from systems import websch, database, compute, aws
from common import enum, pyd_models as pyd
from time import sleep
from datetime import datetime

example_db_settings = dict(
    fqdn_amount=250,
    min_url_amount=5,
    max_url_amount=5,
    )

project_settings = dict(
    name="{}_three_parallel_fetcher".format(datetime.now().strftime("%Y-%m-%d")),
    repetition=1,
    parallel_fetcher=3,
)

case_settings = pyd.CaseSettings(
    logging_mode=None,
    crawling_speed_factor=[10],
    default_crawl_delay=[10],
    parallel_process=[4],
    iterations=[1],
    fqdn_amount=[30],
    url_amount=None,
    long_term_mode=[enum.LTF.large_sites_first],
    short_term_mode=[enum.STF.new_pages_first],
    min_links_per_page=[1],
    max_links_per_page=[1],
    lpp_distribution_type=None,
    internal_vs_external_threshold=[1.0],
    new_vs_existing_threshold=[1.0],
)


def main():
    print("Compute Cases ...")
    settings_collection = compute.create_cases(case_settings, project_settings)
    print("Cases created: {}".format(len(settings_collection)))

    print("Reset Example DB ...")
    websch.delete_example_db()
    websch.generate_example_db(**example_db_settings)
    websch.wait_for_example_db(example_db_settings)

    print("Backup FQDN- & URL-Frontier Tables ...")
    database.backup_table("fqdn_frontiers")
    database.backup_table("url_frontiers")

    for i in range(len(settings_collection)):
        print("* Reset Example DB ...")
        websch.delete_example_db()
        database.restore_table("fqdn_frontiers")
        database.restore_table("url_frontiers")

        print("* Set Fetcher Settings ...")
        print("* Case {}".format(settings_collection[i]))
        websch.set_fetcher_settings(settings_collection[i])

        print("* Create EC2 Instance(s) ...")
        instance_ids = aws.create_instance(project_settings)

        for instance_id in instance_ids:
            file_name = instance_id + ".log"

            file_found = False
            print("* Waiting for {}.log-File in S3 Bucket ...".format(instance_id))
            while not file_found:
                print("-", end="")
                sleep(15)
                file_found = aws.download_file(file_name)

            print("* Terminate EC2 Instance ...")
            aws.terminate_instance(instance_id)

    compute.write_json_file()
    compute.write_csv_file()

    compute.archive_project(project_settings["name"])


if __name__ == "__main__":
    main()
