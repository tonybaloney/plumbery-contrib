import yaml
import logging
from pykwalify.core import Core


def check_existence_of_key(dictionary, key, path):
    try:
        dictionary[key] \
            or raise_KeyError('%s not present' % key)
    except KeyError:
        logging.error("fittings %s missing required links",
                      path)


def raise_KeyError(msg=''): raise KeyError(msg)  #  Don't return anything.


def validate_fittings(file_path):
    with open(file_path, 'r') as document_stream:
        document = document_stream.read()
        for settings in yaml.load_all(document):
            logging.debug("Validating source data %s",
                         settings)

            c = Core(source_data=settings, schema_files=["schema.yaml"])
            c.validate(raise_exception=True)
