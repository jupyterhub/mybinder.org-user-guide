``mybinder.org`` status and reliability
=======================================

This page serves as a source of information for general Binder status
updates, building/launching statistics, and reliability metrics.

Site Reliability Goals
----------------------

As ``mybinder.org`` is a research pilot project, the main goal for the project
is to understand usage patterns and workloads for future project evolution.
While we strive for site reliability and availability, we want our users to
understand the intent of this service is research and we offer no guarantees
of its performance in mission critical uses.

We are still working on defining what the exact goals for uptime and reliability
should be.

.. note::

   The ``mybinder.org`` team can always use more help in maintaining the
   BinderHub deployment that runs this site. If you're interested in getting
   involved, or have any thoughts or suggestions,
   please reach out to us on `our Gitter channel <https://gitter.im/jupyterhub/binder>`_.

Site metrics
------------

Below are two key reliability metrics that give an idea for the health of
the ``mybinder.org`` deployment. Note that you can find many more metrics about
the ``mybinder.org`` deployment at `grafana.mybinder.org <https://grafana.mybinder.org>`_.


.. raw:: html

   <iframe src="https://grafana.mybinder.org/dashboard-solo/db/service-level-objectives?orgId=1&panelId=1&from=1517940977444&to=1518545777444&theme=light" style="width: 100%; height: 200px" frameborder="0"></iframe>
   <br />
   <br />

.. raw:: html

   <iframe src="https://grafana.mybinder.org/dashboard-solo/db/service-level-objectives?orgId=1&panelId=2&from=1517940892627&to=1518545692627&theme=light" style="width: 100%; height: 200px" frameborder="0"></iframe>
