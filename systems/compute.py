from itertools import product
import os
import json


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
    data_string = row[row.find("Stats:")+7: -2].replace("(", "").replace(")", "")
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
