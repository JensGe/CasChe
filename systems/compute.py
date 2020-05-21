from itertools import product

# def create_cases(case_settings):
#     case_settings_reduced = dict()
#
#     for attr, val in vars(case_settings).items():
#         if val is not None:
#             print("key: {}, value(s): {}".format(attr, val))
#             case_settings_reduced[attr] = val
#
#     return dict(itertools.product(*case_settings_reduced.values()))


def create_cases(case_settings):
    case_settings_dict = dict()

    for attr, val in vars(case_settings).items():
        if val is not None:
            case_settings_dict[attr] = val

    settings_collection = []
    for element in dict_product(case_settings_dict):
        settings_collection.append(element)

    return settings_collection


def dict_product(d):
    keys = d.keys()
    for element in product(*d.values()):
        yield dict(zip(keys, element))
