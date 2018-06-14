Status of ``mybinder.org``
==========================

This page displays several graphics that give an idea for the current
status of the `mybinder.org <https://mybinder.org>`_ service. You can find
a more complete set of graphs the reflect the current state of ``mybinder.org``
at `grafana.mybinder.org <https://grafana.mybinder.org>`_.

.. note::

   **If you notice an outage** or strong degradation of service at
   `mybinder.org <https://mybinder.org>`_, please reach out to
   the Binder team at the `Binder gitter channel <https://gitter.im/jupyterhub/binder>`_!

Running Binder sessions
-----------------------

The total number of user sessions running on Binder.

.. raw:: html

   <iframe src="https://grafana.mybinder.org/d-solo/fLoQvRHmk/status?panelId=6&orgId=1&tab=general&theme=light" width="500" height="200" frameborder="0"></iframe>

Binder launch success
---------------------

The percentage of new user sessions that successfully launched. If you see
a dip that sustains itself over time, please alert the Binder team at the
`Binder gitter channel <https://gitter.im/jupyterhub/binder>`_.

.. raw:: html

   <iframe src="https://grafana.mybinder.org/d-solo/fLoQvRHmk/status?panelId=2&orgId=1&tab=general&theme=light" width="500" height="200" frameborder="0"></iframe>

Launch time percentiles
-----------------------

The amount of time it takes for a Binder session to successfully launch.
Note that if a Docker image for a repository is not on a node, the launch
time takes much longer.

.. raw:: html

   <iframe src="https://grafana.mybinder.org/d-solo/fLoQvRHmk/status?panelId=4&orgId=1&tab=general&theme=light" width="500" height="200" frameborder="0"></iframe>
