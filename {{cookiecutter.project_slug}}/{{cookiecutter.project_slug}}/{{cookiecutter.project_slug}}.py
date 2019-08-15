# -*- coding: utf-8 -*-

"""Main module for {{ cookiecutter.project_slug }}.py.

Notes
-----
Code documentation follows `numpydoc <https://github.com/numpy/numpy/tree/master/doc/sphinxext>`_ style.

See Also
--------
A nice `numpydoc example.py <https://numpydoc.readthedocs.io/en/latest/example.html#example>`_.

"""


def hello(name="{{ cookiecutter.author }}", project="{{ cookiecutter.project_slug }}"):
    """TODO: Add a one-line summary of the function here.

    TODO: Add a multi-line description of function here if needed.

    Parameters
    ----------
    name : str
        A name of a person.
    project : str
        A name of a project.

    Notes
    -----
    Notes about function.

    References
    ----------
    Cite the relevant references, e.g. [1]_.

    .. [1] Wilson G, Aruliah DA, Brown CT, Chue Hong NP, Davis M, Guy RT, et al. (2014) Best Practices for Scientific Computing. PLoS Biol 12(1): e1001745. https://doi.org/10.1371/journal.pbio.1001745

    """

    print("Hello {}!".format(name))
    print("Good luck on your {} project!".format(project))


if __name__ == "__main__":
    hello()
