from systems import websch, database

""" ToDo
[x] create db_example
    [x] reset (request WebSch)
    [x] generate example db
[x] backup db_example
[ ] create all cases (FetcherSettings)
[ ] for each FetcherSetting:
    [ ] restore db_example
    [ ] set current FetcherSetting
    [ ] reboot / create FetSim Instance
    [ ] download Log from S3 and name corresponding to FetcherSettings
[ ] parse results

"""


def main():
    # websch.delete_example_db()
    # websch.generate_example_db(fqdn_amount=30, min_url_amount=5, max_url_amount=5)
    #
    # database.backup_table("fqdn_frontiers")
    # database.backup_table("url_frontiers")

    database.restore_table("fqdn_frontiers")
    database.restore_table("url_frontiers")

if __name__ == '__main__':
    main()
