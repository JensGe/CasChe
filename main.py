from systems import websch

""" ToDo
[x] create db_example
    [x] reset (request WebSch)
    [x] generate example db
[ ] backup db_example
[ ] create all cases (FetcherSettings)
[ ] for each FetcherSetting:
    [ ] restore db_example
    [ ] set current FetcherSetting
    [ ] reboot / create FetSim Instance
    [ ] download Log from S3 and name corresponding to FetcherSettings
[ ] parse results

"""


def main():
    websch.delete_example_db()
    websch.generate_example_db(fqdn_amount=30, min_url_amount=5, max_url_amount=5)



if __name__ == '__main__':
    main()
