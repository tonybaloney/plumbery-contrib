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


def validate_fittings(file_path, readme, subdir):
    with open(file_path, 'r') as document_stream:
        document = document_stream.read()
        for settings in yaml.load_all(document):
            logging.info("Validating source data %s",
                         settings)

            c = Core(source_data=settings, schema_files=["schema.yaml"])
            c.validate(raise_exception=True)

            readme += "\n### [%s](%s) \n\n<img src='%s' style='width: 64px;'/>\n%s" % (
                settings['information'][0],
                settings['links']['documentation'],
                'https://raw.githubusercontent.com/DimensionDataCBUSydney/plumbery-contrib/master/%s/icon.png' % subdir.replace('\\','/'),
                '\n'.join(settings['information'][0:])
            )
            # parameters may break remaining documents
            break