backports.shutil_get_terminal_size
==================================


.. image:: http://img.shields.io/pypi/v/backports.shutil_get_terminal_size.svg?style=flat-square
    :target: https://pypi.python.org/pypi/backports.shutil_get_terminal_size

.. image:: http://img.shields.io/pypi/dm/backports.shutil_get_terminal_size.svg?style=flat-square
    :target: https://pypi.python.org/pypi/backports.shutil_get_terminal_size
    
.. image:: http://img.shields.io/travis/chrippa/backports.shutil_get_terminal_size.svg?style=flat-square
    :target: http://travis-ci.org/chrippa/backports.shutil_get_terminal_size


A backport of the `get_terminal_size`_ function from Python 3.3's shutil.

Unlike the original version it is written in pure Python rather than C,
so it might be a tiny bit slower.

.. _get_terminal_size: https://docs.python.org/3/library/shutil.html#shutil.get_terminal_size


Example usage
-------------

.. code-block:: pycon

    >>> from backports.shutil_get_terminal_size import get_terminal_size
    >>> get_terminal_size()
    terminal_size(columns=105, lines=33)

