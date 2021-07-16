Installation
------------

First install package

.. code:: shell

    $ pip install django-sage-streaming

Then add ``sage_stream`` to INSTALLED\_APPS in settings.py

.. code:: python

    INSTALLED_APPS = [
      ...
      'sage_stream',
      ...
    ]

Also make sure you have ``rest_framework`` in INSTALLED\_APPS

.. code:: python

    INSTALLED_APPS = [
      ...
      'rest_framework',
      ...
    ]
