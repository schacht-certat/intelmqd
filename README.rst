######################################################
THIS WAS A PROOF OF CONCEPT AND HAS NOW BEEN ARCHIVED!
######################################################

The functionality is provided by `intelmq-api <https://github.com/certtools/intelmq-api>`_.


****************************
IntelMQ API Proof of Concept
****************************

Howto Test
----------

Set up your environment, for example using ``virtualenv``:

.. code-block:: bash

   python3 -m venv ~/.virtualenvs/intelmqd
   source ~/.virtualenvs/intelmqd/bin/activate


Install dependencies:

.. code-block:: bash

   pip install -r data/requirements.txt


Run the API:

.. code-block:: bash

   python3 app/main.py

Whats implemented?
------------------

You can see the API docs on ``localhost:42432/docs``; The ``/botnet``, ``/bot`` and ``/config`` routes are implemented. Using the ``/config`` route you can ``PUT`` configuration.

TODO
----

Authentication
