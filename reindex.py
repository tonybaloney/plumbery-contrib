import yaml
import os
import logging
import sys
import json

from validation import validate_fittings

LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}

if len(sys.argv) > 1:
    level_name = sys.argv[1]
    level = LEVELS.get(level_name, logging.NOTSET)
    logging.basicConfig(level=level)


complete_index = {}


def read_fitting(file_path):
    with open(file_path) as fitting_f:
        plan = fitting_f.read()
        documents = plan.split('\n---')
        index = 0
        for document in documents:
            index += 1
            if '\n' in document and index == 1:
                settings = yaml.load(document)
                logging.info("Validated fittings %s", file_path)
    return settings


def get_fittings(directory, name, description):
    fittings = []
    # Check and load directory.
    for subdir, dirs, files in os.walk("fittings/"+directory):
        logging.info("Sub-directory %s", subdir)
        for dir in dirs:
            logging.info("Found directory %s", dir)

        for file in files:
            if file == "fittings.yaml":
                # check the yaml
                file_path = os.path.join(subdir, file)
                validate_fittings(file_path)
                fittings.append({"directory": subdir,
                                 "icon": os.path.join(subdir, "icon.png")})
    return fittings


with open("fittings/categories.yaml", "r") as categories_f:
    docs = yaml.load(categories_f)
    complete_index['Categories'] = [{
        'name': category['name'],
        'description': category['description'],
        'fittings': [
            {'name': fitting['directory'].replace('\\', '/')} for fitting in get_fittings(category['directory'],
                                                         category['name'],
                                                         category['description'])
            ]
            } for category in docs['categories']]
    for category in docs['categories']:
        get_fittings(
            category['directory'],
            category['name'],
            category['description'])


with open("index.json", "w") as index_f:
    index_f.write(json.dumps(complete_index))
