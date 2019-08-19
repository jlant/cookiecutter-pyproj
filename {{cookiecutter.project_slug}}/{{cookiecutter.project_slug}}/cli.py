# -*- coding: utf-8 -*-

"""Click command line interface for {{ cookiecutter.project_slug }}.

Notes
-----
Click is a great Python package for creating nice command line interfaces.
Please see `Click documentation <http://click.pocoo.org/>`_.
"""

import sys
import click

import {{cookiecutter.project_slug}}


@click.command()
@click.option("--verbose", is_flag=True, help="Print detailed results from analysis/model")
def main(verbose):
    """Command line interface for iris.

    Run all analysis, models, and/or main script from a command line interface.
    """
    click.echo("Running analysis from a Click command line interface")
    {{cookiecutter.project_slug}}.main()
    click.echo("Click allows you to easily add various commands and options "
               "as you see fit.")
    click.echo()

    if verbose:
        click.echo("Verbose mode is on.")
        click.echo("Can print more detailed results from your analysis/model.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
