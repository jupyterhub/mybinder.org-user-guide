.. _howto/repo_data:

=========================================
Track repository data on ``mybinder.org``
=========================================

The mybinder.org team runs a service that provides repository-level data
about all of the binders that run each day. This is called the
**mybinder.org event analytics archive**. You can use this to track
how often people are clicking your Binder links and launching your
Binder repository (or, for aggregating activity across many repositories).


How to access the event analytics archive
=========================================

You can access the event analytics archive at
`archive.analytics.mybinder.org <https://archive.analytics.mybinder.org>`_

For information about the structure of this dataset, and a description of
how you can read-in the data in order to analyze it, see the
`mybinder SRE guide instructions <https://mybinder-sre.readthedocs.io/en/latest/analytics/events-archive.html>`_.


An example repository to show off analyses
==========================================

To give you a little inspiration, check out
`the binderlyzer binder <https://mybinder.org/v2/gh/betatim/binderlyzer/master>`_.
This is a Binder that goes through a simple analysis of Binder repositories
using the events archive. It shows how to access it, and gives an idea for
questions you can ask with this data!


If you do something interesting or fun with the event analytics archive, please
let us know! We provide this resource in the hopes that it gives people insight
into the activity going on in Binder land, and would love to hear about anything
interesting you find.