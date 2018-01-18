Binder Usage Guidelines
=======================

This page details some guidelines and policies that we follow at ``mybinder.org``.

Temporary Banning
-----------------

Temporary banning means that `mybinder.org` will stop building / serving Binder
sessions for a given repository. This usually happens because of some
undesired behavior with the repository. Some examples of behavior that could
result in temporary banning include:

* A large, unexpected spike in traffic that persists over time.
* Sessions that routinely use a large amount of CPU.
* Sessions that attempt to perform a lot of outgoing networking traffic.

The ``mybinder.org`` team uses the following workflow in discussing / deciding
when to temporarily ban a repository:

* An issue is created to document why a repo (or group of repos) is being banned
* A PR that implements the ban is opened
* A "bans" tag notes any PRs that created a ban
* The issue stays open until the ban is lifted

If you are temporarily banned, contact us on the
`Gitter Channel <https://gitter.im/jupyterhub/binder>`_ or
`Open an Issue <https://github.com/jupyterhub/mybinder.org-deploy/issues>`_ to discuss
how to un-ban the repository.

Reporting Abuse
---------------

If you'd like to report any abuse of the ``mybinder.org`` service, please
`click here to send an abuse report <mailto:binder-team@googlegroups.com?subject=[ABUSE]<your-message-here>`_. 
