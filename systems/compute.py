from itertools import product
import os
import json
import csv
import shutil
from datetime import datetime


def create_cases(case_settings, project_settings):
    case_settings_dict = dict()

    for attr, val in vars(case_settings).items():
        if val is not None:
            case_settings_dict[attr] = val

    settings_collection = []
    for element in dict_product(case_settings_dict):
        settings_collection.extend(element for _ in range(project_settings["repetition"]))

    return settings_collection


def dict_product(d):
    keys = d.keys()
    for element in product(*d.values()):
        yield dict(zip(keys, element))


def get_fetcher_settings(row):
    fetcher_settings = json.loads(row[row.find("{") :].replace("'", '"'))
    return fetcher_settings


def get_iteration_results(row):
    data_string = row[row.find("Stats:") + 7 : -2].replace("(", "").replace(")", "")
    data_list = data_string.split(", ")
    for i in range(len(data_list)):
        data_list[i] = data_list[i].split(" ")
    data_dict = {k[0]: k[1] + " " + k[2] for k in data_list}
    return data_dict


def get_stats_results(row):
    data_string = row[row.find("Stats:") + 7:]
    data_list = data_string.split(", ")
    for i in range(len(data_list)):
        data_list[i] = data_list[i].split(": ")
    data_dict = {k[0]: k[1] for k in data_list}
    data_dict["db_access_time"] = row.split(" ")[0] + " " + row.split(" ")[1]
    return data_dict


def jsonify_results():
    results = list()

    for subdir, dirs, files in os.walk("fetsim-logs"):
        for file in files:
            iteration_stats = list()
            db_stats = list()
            mod_date = os.path.getmtime("fetsim-logs/" + file)
            if file.endswith('.log'):
                with open(subdir + "/" + file, "r") as f:
                    for row in f:
                        if "Fetcher Settings" in row:
                            fetcher_settings = get_fetcher_settings(row)
                        if "Iteration Stats" in row:
                            iteration_stats.append(get_iteration_results(row))
                        if "DB Stats" in row:
                            db_stats.append(get_stats_results(row))
                for i in range(len(iteration_stats)):
                    results.append(
                        dict(
                            fetcher_settings=fetcher_settings,
                            iteration_stats=iteration_stats[i],
                            db_stats=db_stats[i],
                        )
                    )
    return results


def write_json_file():
    with open("fetsim-logs/results.json", "w") as json_file:
        json.dump(jsonify_results(), json_file)


def write_csv_file():
    with open("fetsim-logs/results.csv", "w", newline="") as csv_file:
        field_names = [
            "logging_mode",
            "crawling_speed_factor",
            "default_crawl_delay",
            "parallel_process",
            "parallel_fetcher",
            "iterations",
            "fqdn_amount",
            "url_amount",
            "min_links_per_page",
            "max_links_per_page",
            "lpp_distribution_type",
            "internal_vs_external_threshold",
            "new_vs_existing_threshold",
            "short_term_prio_mode",
            "long_term_prio_mode",
            "long_term_part_mode",
            "load",
            "fetch",
            "fetch_cpu",
            "submit",
            "db_access_time",
            "db_frontier_amount",
            "db_url_amount",
            'db_avg_freshness',
            'db_visited_ratio',
            'db_fqdn_hash_range'
        ]

        writer = csv.DictWriter(csv_file, fieldnames=field_names, delimiter=";")
        writer.writeheader()

        results = jsonify_results()

        for run in results:
            writer.writerow(
                {**run["fetcher_settings"], **run["iteration_stats"], **run["db_stats"]}
            )


def archive_project(settings):
    file_iter = 1
    filename = "{}_{}".format(settings["date"], settings["name"])
    org_filename = filename
    while os.path.isfile("finished_results/{}.zip".format(filename)):
        file_iter += 1
        filename = org_filename + "_" + str(file_iter)

    shutil.make_archive("finished_results/{}".format(filename), "zip", "fetsim-logs")
    shutil.rmtree("fetsim-logs")



