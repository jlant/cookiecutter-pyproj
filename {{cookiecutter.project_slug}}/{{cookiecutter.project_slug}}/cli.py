# -*- coding: utf-8 -*-

"""Click command line interface for {{ cookiecutter.project_slug }}.

Notes
-----
Click is a nice and simple Python package for creating command line
interfaces.
Please see click documentation at http://click.pocoo.org/
"""

import sys
import click

import {{cookiecutter.project_slug}}


@click.command()
def main(args=None):
    """Command line interface for {{ cookiecutter.project_slug }}."""

    {{cookiecutter.project_slug}}.hello()
    click.echo()
    click.echo("The following are automatically setup to help you get up and "
               "running on your project quickly:")
    click.echo("  * A Click command line interface in {{ cookiecutter.project_slug}}.cli.main")
    click.echo("  * Pytest suite in the `tests` directory.")
    click.echo("  * Sphinx documentation in the `docs` directory.")
    click.echo("  * Makefile for easy running of tests and generating project documentation.")
    click.echo("  * Template README.md file.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
