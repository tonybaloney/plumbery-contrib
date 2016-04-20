# Plumbery-Contrib

[![Build status](https://img.shields.io/travis/DimensionDataCBUSydney/plumbery-contrib.svg)](https://travis-ci.org/DimensionDataCBUSydney/plumbery-contrib)  ![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)


A public repository of templates for provisioning applications into the Dimension Data Cloud

## Using

You will need to install [Plumbery](https://pypi.python.org/pypi/plumbery) from PyPi to use these examples

Then you can download and run any of the examples in this repository.

```bash
git clone https://github.com/DimensionDataCBUSydney/plumbery-contrib.git
cd plumbery-contrib/fittings/containers/docker
python -m plumbery fittings.yaml deploy
```

## Contributing

This repository accepts pull-requests, if you wish to share your own application template:

* Create a fork of this repository and create your application
 * Choose the category of your application - if the category does not exist, simple create a new folder and update fittings/categories.yaml
 * Create a folder for your fittings template
 * Create the `fittings.yaml` file in your folder, see [documentation](https://developer.dimensiondata.com/display/PLUM/Fittings+schema+documentation) for schema documentation
 * Include a README.md with the instructions for your template
 * Check your syntax using `python validation.py <path to your fittings file>.yaml`
 * Reindex the library `python reindex.py info`
* Commit your code
* Create a pull-request
