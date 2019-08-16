# -*- coding: utf-8 -*-

"""Main module for {{ cookiecutter.project_slug }}.py.

Notes
-----
Code documentation follows `numpydoc <https://github.com/numpy/numpy/tree/master/doc/sphinxext>`_ style.

| Can add math equations to docstrings using LaTeX!
|
| Sample standard deviation:

.. math:: s^2 = \\sqrt{\\sum_{i=1}^n (y_i - \\bar{y})^2}

Use raw string (r"") or double slashes along with Chrome or Firefox for proper rendering.

See Also
--------
`numpydoc example.py <https://numpydoc.readthedocs.io/en/latest/example.html#example>`_.

`Math support in Sphinx <https://shimizukawa-sphinx.readthedocs.io/en/latest/ext/math.html#module-sphinx.ext.mathbase>`_.

References
----------
Cite the relevant references in this section.

Such as this recommended paper: `Best Practices in Scientific Computing`_.

.. _Best Practices in Scientific Computing: https://doi.org/10.1371/journal.pbio.1001745

"""


def hello(name="{{ cookiecutter.author }}", project="{{ cookiecutter.project_slug }}"):
    """Say hello.

    Say hello to someone and wish them good luck on their project.

    Parameters
    ----------
    name : str
        A name of a person.
    project : str
        A name of a project.

    Notes
    -----
    Just a sample function to show docstrings with numpydoc.

    """
    print()
    print("Hello {}!".format(name))
    print("Good luck on your {} project!".format(project))
    print()


def main():
    """Main analysis function.

    Main function for running analysis functions, models, etc.
    """
    hello()
    print("For demo purposes only, just printing output of a simple hello() "
          "function above.")
    print("Replace with your analysis functions, models, etc.")
    print()


if __name__ == "__main__":
    main()
