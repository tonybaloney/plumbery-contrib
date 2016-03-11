import yaml
import os
import logging
import sys

LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}

if len(sys.argv) > 1:
    level_name = sys.argv[1]
    level = LEVELS.get(level_name, logging.NOTSET)
    logging.basicConfig(level=level)


def raise_KeyError(msg=''): raise KeyError(msg)  # Don't return anything.


def check_existence_of_key(dictionary, key, path):
    try:
        dictionary[key] \
            or raise_KeyError('%s not present' % key)
    except KeyError:
        logging.error("fitting %s missing required links",
                      path)

with open("fittings/categories.yaml", "r") as categories_f:
    docs = yaml.load(categories_f)
    for category in docs['categories']:
        # Check and load directory.
        for subdir, dirs, files in os.walk("fittings/"+category['directory']):
            logging.info("Subdirectory %s", subdir)

            for dir in dirs:
                logging.info("Found directory %s", dir)

            for file in files:
                if file == "fitting.yaml":
                    # check the yaml
                    file_path = os.path.join(subdir, file)
                    with open(file_path) as fitting_f:
                        fitting_collection = yaml.load_all(fitting_f)
                        logging.info("Validated fitting %s",
                                     file_path)
                        for idx, fitting in enumerate(fitting_collection):
                            if idx == 0:
                                # Check existence of docs
                                check_existence_of_key(fitting, 'links', file_path)
                                check_existence_of_key(fitting, 'information', file_path)
