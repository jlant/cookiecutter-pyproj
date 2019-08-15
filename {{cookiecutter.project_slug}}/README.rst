{{ cookiecutter.project_slug }}
===============================

{{ cookiecutter.project_description }}


Overview
--------
TODO: Add overview of project.


The following is the structure of the Python_ project::

    ├── {{cookiecutter.project_slug}}               Source code directory. {{cookiecutter.project_slug}} is 
    │                                               replaced with `project_slug` used in cookiecutter prompt
    │   ├── __init__.py                             Makes project a Python package
    │   ├── {{cookiecutter.project_slug}}.py        Main project module.
    │   └── cli.py                                  Command line interface using Click
    │
    ├── data                                        Original (raw) and final (processed) data sets
    │   └── readme-dataset.txt                      Template "readme.txt" style for metadata, replace "dataset"
    │                                               with name of dataset
    │
    ├── docs                                        Project and code documentation with Sphinx
    │   └── _static                                 Sphinx directory for used for styling and images
    │                                               Contains files to document project analysis and changes
    │   └── notebooks                               Jupyter notebooks used for data exploration and computational narrative
    │       └── 01-exploratory-analysis.ipynb       Initial notebook for data exploration
    │   └── *.rst                                   Various restructured text files linked together in `index.rst`
    │
    ├── tests                                       Tests for source code for use with pytest
    │   ├── __init__.py                             Makes tests directory a Python package for use with fixtures
    │   └── test_{{cookiecutter.project_slug}}.py   Sample test file for main project module
    │
    ├── .gitignore
    ├── AUTHORS.md
    ├── Makefile                                    Makefile, list commands with `make help`
    ├── LICENSE                                     A sample MIT License, change as you like
    ├── README.md                                   README for the project
    ├── requirements.txt                            The requirements file for reproducing the Python analysis environment
    ├── setup.py                                    Python installation file



Requirements
------------
TODO: Update `requirements.txt` file.

Install requirements using python 3.x::

    $ pip3 install -r requirements.txt


Documentation
-------------
Project documentation is made using Sphinx_.  

Documentation can be found in the `docs` directory.  


Update project documentation using toplevel Makefile.::

    $ make docs


Jupyter Notebooks
-----------------
Jupyter_ notebooks can be found within the `docs/notebooks` directory.  

The notebooks are embedded in the project documentation using nbsphinx_.


Tests
-----
A suite of tests were built using pytest_.

Run the test suite using pytest_ directly.::

    $ pytest tests/

Run the test suite using toplevel Makefile.::

    $ make tests


Author
------
{{ cookiecutter.author }} <{{ cookiecutter.email }}>



.. _Python: https://www.python.org/
.. _Jupyter: https://jupyter.org/
.. _pytest: https://docs.pytest.org/en/latest/
.. _Sphinx: http://www.sphinx-doc.org/en/master/
.. _nbsphinx: https://nbsphinx.readthedocs.io/en/0.4.2/index.html
