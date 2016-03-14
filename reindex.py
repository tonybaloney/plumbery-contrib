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


def raise_KeyError(msg=''): raise KeyError(msg)  #  Don't return anything.


def check_existence_of_key(dictionary, key, path):
    try:
        dictionary[key] \
            or raise_KeyError('%s not present' % key)
    except KeyError:
        logging.error("fittings %s missing required links",
                      path)
readme = ""

with open("fittings/categories.yaml", "r") as categories_f:
    docs = yaml.load(categories_f)
    for category in docs['categories']:
        readme += "\n## %s\n\n%s" % (
            category['name'], category['description'])
        # Check and load directory.
        for subdir, dirs, files in os.walk("fittings/"+category['directory']):
            logging.info("Subdirectory %s", subdir)

            for dir in dirs:
                logging.info("Found directory %s", dir)

            for file in files:
                if file == "fittings.yaml":

                    # check the yaml
                    file_path = os.path.join(subdir, file)
                    with open(file_path) as fitting_f:

                        plan = fitting_f.read()
                        documents = plan.split('\n---')
                        for document in documents:
                            if '\n' in document:
                                settings = yaml.load(document)
                                logging.info("Validated fittings %s",
                                             file_path)

                                # Check existence of docs
                                check_existence_of_key(settings,
                                                       'links', file_path)
                                check_existence_of_key(settings,
                                                       'information', file_path)
                                readme += "\n### [%s](%s) \n\n<img src='%s' style='width: 64px;'/>\n%s" % (
                                    settings['information'][0],
                                    settings['links']['documentation'],
                                    'https://raw.githubusercontent.com/DimensionDataCBUSydney/plumbery-contrib/master/%s/icon.png' % subdir.replace('\\','/'),
                                    '\n'.join(settings['information'][0:])
                                )
                                # parameters may break remaining documents
                                break
with open("INDEX.md", "w") as readme_f:
    readme_f.write(readme)