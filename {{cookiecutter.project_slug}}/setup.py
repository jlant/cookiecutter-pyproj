#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup


with open("README.md") as readme_file:
    readme = readme_file.read()


requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    "pytest",
]


setup(
    author="{{ cookiecutter.author }}",
    author_email="{{ cookiecutter.email }}",
    description="{{ cookiecutter.project_description }}",
    entry_points={
        "console_scripts": [
            "{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli.main",
        ],
    },
    include_package_data=True,
    install_requires=requirements,
    keywords="{{ cookiecutter.project_slug }}",
    long_description=readme,
    name="{{ cookiecutter.project_slug }}",
    packages=find_packages(include=["{{ cookiecutter.project_slug }}"]),
    test_suite="tests",
    tests_require=test_requirements,
    zip_safe=False,
)
