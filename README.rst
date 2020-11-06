############################
IntelMQ API Proof of Concept
############################

Howto Test
==========

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
==================

You can see the API docs on ``localhost:42432/docs``; The ``/botnet`` and the ``/bot`` routes are implemneted. The ``/config`` route is TBD.
