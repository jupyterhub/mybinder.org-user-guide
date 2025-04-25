mybinder.org status
===================

This page displays several graphics that give an idea for the current
status of the `mybinder.org <https://mybinder.org>`_ service. You can find
a more complete set of graphs the reflect the current state of ``mybinder.org``
at `grafana.mybinder.org <https://grafana.mybinder.org>`_.

.. note::

   **If you notice an outage** or strong degradation of service at
   `mybinder.org <https://mybinder.org>`_, please reach out to
   the Binder team at the `Binder Zulip JupyterHub chat <https://jupyter.zulipchat.com/#narrow/channel/469744-jupyterhub>`_!

Federation status
-----------------

The following table lists BinderHub deployments in the mybinder.org
federation, along with the status of each. For more information about
the BinderHub federation, who is in it, how to join it, etc, see
`the mybinder federation page <https://mybinder.readthedocs.io/en/latest/about/federation.html>`_.

.. update fedUrls in _static/status.js

==========================  ========  ===============  ==============  =============== =====
  URL                       Response  Docker registry  JupyterHub API  User/Build Pods Quota
==========================  ========  ===============  ==============  =============== =====
ovh.mybinder.org
notebooks.gesis.org/binder
binder.curvenote.dev
==========================  ========  ===============  ==============  =============== =====

.. raw:: html

   <script src="../_static/status.js" type="text/javascript">
   </script>


Running Binder sessions
-----------------------

The total number of user sessions running on Binder.

.. raw:: html

   <iframe src="http://grafana.mybinder.org/d-solo/3SpLQinmk/1-overview?theme=light&orgId=1&from=now-6h&to=now&timezone=browser&var-cluster=GESIS&panelId=31&__feature.dashboardSceneSolo" width="500" height="240" frameborder="0"></iframe>

Binder launch success
---------------------

The percentage of new user sessions that successfully launched. If you see
a dip that sustains itself over time, please alert the Binder team at the
`Binder gitter channel <https://gitter.im/jupyterhub/binder>`_.

.. raw:: html

   <iframe src="http://grafana.mybinder.org/d-solo/fZWsQmnmz/pod-activity?orgId=1&var-cluster=2i2c&from=now-6h&to=now&timezone=browser&theme=light&panelId=9&__feature.dashboardSceneSolo" width="500" height="200" frameborder="0"></iframe>

.. raw:: html

   <iframe src="http://grafana.mybinder.org/d-solo/fZWsQmnmz/pod-activity?orgId=1&var-cluster=GESIS&from=now-6h&to=now&timezone=browser&theme=light&panelId=9&__feature.dashboardSceneSolo" width="500" height="200" frameborder="0"></iframe>

Launch time percentiles
-----------------------

The amount of time it takes for a Binder session to successfully launch.
Note that if a Docker image for a repository is not on a node, the launch
time takes much longer.

.. raw:: html

   <iframe src="http://grafana.mybinder.org/d-solo/3SpLQinmk/1-overview?orgId=1&var-cluster=2i2c&from=now-6h&to=now&timezone=browser&theme=light&panelId=28&__feature.dashboardSceneSolo" width="500" height="200" frameborder="0"></iframe>

.. raw:: html

   <iframe src="http://grafana.mybinder.org/d-solo/3SpLQinmk/1-overview?orgId=1&var-cluster=GESIS&from=now-6h&to=now&timezone=browser&theme=light&panelId=28&__feature.dashboardSceneSolo" width="500" height="200" frameborder="0"></iframe>

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

   <iframe src="https://grafana.mybinder.org/d-solo/KPtswm7ik/service-level-objectives?orgId=1&theme=light&panelId=3&from=now-7d&to=now" width="450" height="200" frameborder="0"></iframe>
