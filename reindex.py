import yaml
import os
import logging
import sys

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
                    validate_fittings(os.path.join(subdir, file), readme, subdir)

with open("INDEX.md", "w") as readme_f:
    readme_f.write(readme)