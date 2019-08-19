{{ cookiecutter.project_slug }}
===============================

{{ cookiecutter.project_description }}


Overview
--------
TODO: Add overview of project.


Project Layout
--------------
The following is the layout of the project along with a description of its contents::

   |-- AUTHORS.rst                                 List of authors working on the project
   |-- Makefile                                    Top-level Makefile, list commands with `make help`
   |-- README.rst                                  Project README
   |-- data                                        Directory for raw and processed data with corresponding metadata
   |-- docs                                        Directory for project and code documentation using Sphinx
   |   |-- Makefile                                Sphinx Makefile
   |   |-- _static                                 Directory for project website styles and project images/figures
   |   |-- analysis.rst                            File to describe detailed project analysis
   |   |-- authors.rst                             Copy of AUTHORS.rst from top-level directory
   |   |-- changelog.rst                           List of dated notes about project changes
   |   |-- code.rst                                File to automatically document your code docstrings
   |   |-- conf.py                                 Sphinx configuration file
   |   |-- index.rst                               Main project documentation page, links all documentation *.rst files
   |   |-- install.rst                             File to describe how to install project requirements
   |   |-- make.bat                                Sphinx make.bat file
   |   |-- notebooks                               Directory containing Jupyter notebooks used for data exploration and communicating a computational narrative
   |   |   `-- 01-exploratory-analysis.ipynb       Sample first Jupyter notebook on project exploratory analysis, can use 01-*, 02-*, ... for logical ordering
   |   |-- notebooks.rst                           File to list Jupyter notebooks contained in `notebooks` directory for proper linking in project documentation
   |   `-- overview.rst                            File to provide a high-level overview of the project
   |-- <project_name>                              Directory for project source code
   |   |-- __init__.py                             Python file to make source code directory a Python package
   |   |-- cli.py                                  Command line interface file using Click
   |   `-- <project_name>.py                       Main project module
   |-- requirements.txt                            List of project requirements to reproduce project environment
   |-- setup.py                                    Python installation file, used if project source code is to be installed on another machine
   `-- tests                                       Directory for all tests of source code using pytest (as default)
       |-- __init__.py                             Python file to make tests directory a Python package
       `-- test_<project_name>.py                  Sample test file for source code




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
