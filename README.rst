Replace ``readline`` for python on OS X
=======================================

Replace system ``readline`` by the one from `pypi
<https://pypi.python.org/pypi/readline>`_.

Usage
-----

::

  $ osx_replace_readline.py python

I use `pythonz <https://github.com/saghul/pythonz/>`_. Run this once per
python::

    $ osx_replace_readline.py $PYTHONZ/pythons/CPython-x.y.z/bin/python


Requirements
------------

``virtualenv``


Warning
-------

This messes with your system python. Use at your own risk


License
-------

MIT
