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

Federation status
-----------------

The following table lists BinderHub deployments in the mybinder.org
federation, along with the status of each. For more information about
the BinderHub federation, who is in it, how to join it, etc, see
`the BinderHub federation page <https://binderhub.readthedocs.io/en/latest/federation/federation.html>`_.

==========================  ========  ===============  ==============  =============== =====
  URL                       Response  Docker registry  JupyterHub API  User/Build Pods Quota
==========================  ========  ===============  ==============  =============== =====
gke.mybinder.org
ovh.mybinder.org
gesis.mybinder.org
turing.mybinder.org
==========================  ========  ===============  ==============  =============== =====

.. raw:: html

   <script>
   var fedUrls = [
         "https://gke.mybinder.org",
         "https://ovh.mybinder.org",
         "https://gesis.mybinder.org",
         "https://turing.mybinder.org",
   ]

   // Use a dictionary to store the rows that should be updated
   var urlRows = {};
   fedUrls.forEach((url) => {
      document.querySelectorAll('tr').forEach((tr) => {
         if (tr.textContent.includes(url.replace('https://', ''))) {
            urlRows[url] = tr;
         };
      });
   });

   fedUrls.forEach((url) => {
         var urlHealth = url + '/health'
         var urlPrefix = url.split('//')[1].split('.')[0]

         // Query the endpoint and update health icon
         var row = urlRows[url];
         let [fieldUrl, fieldResponse, fieldRegistry, fieldHub, fieldPods, fieldQuota] = row.querySelectorAll('td')
         $.getJSON(urlHealth, {})
            .done((resp) => {
               if (resp['ok'] == false) {
                     setStatus(fieldResponse, 'fail')
               } else {
                     setStatus(fieldResponse, 'success')
               }

               let [respReg, respHub, respQuota] = resp['checks']

               if (respReg == false) {
                     setStatus(fieldRegistry, 'fail')
               } else {
                     setStatus(fieldRegistry, 'success')
               }

               if (respHub == false) {
                     setStatus(fieldHub, 'fail')
               } else {
                     setStatus(fieldHub, 'success')
               }

               fieldPods.textContent = `${respQuota['user_pods']}/${respQuota['build_pods']}`
               fieldQuota.textContent = `${respQuota['quota']}`
            })
            .fail((resp) => {
                  setStatus(fieldResponse, 'fail')
         });
   })

   var setStatus = (td, kind) => {
      if (kind == "success") {
         td.textContent = "Success";
         td.style.color = "green";
      } else {
         td.textContent = "Fail";
         td.style.color = "red";
      }
   }

   </script>


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

   <iframe src="https://grafana.mybinder.org/d-solo/KPtswm7ik/service-level-objectives?orgId=1&refresh=1m&from=1601224257009&to=1601829057011&theme=light&panelId=3" width="450" height="200" frameborder="0"></iframe>