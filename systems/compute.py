from itertools import product
import os, json, csv


def create_cases(case_settings, repetition: int = 1):
    case_settings_dict = dict()

    for attr, val in vars(case_settings).items():
        if val is not None:
            case_settings_dict[attr] = val

    settings_collection = []
    for element in dict_product(case_settings_dict):
        settings_collection.extend(element for _ in range(repetition))

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


def jsonify_results():
    results = list()
    for subdir, dirs, files in os.walk("fetsim-logs"):
        for file in files:
            with open(subdir + "/" + file, "rt") as f:
                for row in f:
                    if "Fetcher Settings" in row:
                        fetcher_settings = get_fetcher_settings(row)
                    if "Iteration Stats" in row:
                        iteration_stats = get_iteration_results(row)
            results.append(
                dict(fetcher_settings=fetcher_settings, iteration_stats=iteration_stats)
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
            "iterations",
            "fqdn_amount",
            "url_amount",
            "min_links_per_page",
            "max_links_per_page",
            "lpp_distribution_type",
            "internal_vs_external_threshold",
            "new_vs_existing_threshold",
            "long_term_mode",
            "short_term_mode",
            "load",
            "fetch",
            "fetch_cpu",
            "submit",
        ]

        writer = csv.DictWriter(csv_file, fieldnames=field_names, delimiter=";")
        writer.writeheader()

        results = jsonify_results()

        for run in results:
            writer.writerow({**run["fetcher_settings"], **run["iteration_stats"]})

