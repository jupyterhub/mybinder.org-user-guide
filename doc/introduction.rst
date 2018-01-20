Welcome to the Binder documentation
===================================

For a quick introduction to Binder, and a demonstration of how you can
make a Binder-ready repository, click the Binder link below:

.. image:: https://mybinder.org/badge.svg
   :target: https://mybinder.org/v2/gh/binder-examples/zero-to-binder/master?filepath=intro-to-binder.ipynb

What can I do with Binder?
--------------------------

Binder makes it simple to generate reproducible computing environments from a
Git repository. Binder uses the BinderHub technology to generate a Docker
image from this repository. The image will have all the components that you
specify along with the Jupyter Notebooks inside. You will be able to share a URL
with users that can immediately begin interacting with this environment via the
cloud.

Generating a sharable Binder link
---------------------------------

You may share a link that generates a Binder. To generate a link for your
Binder repository, type in the URL of the repository in the Binder UI and
click the small carrot next to the ``Launch`` button. This will open a popup
where you can display and select the text for your link.

The link structure is::

   https://beta.mybinder.org/v2/gh/<org-name>/<repo-name>/<branch|commit|tag>?filepath=<path/to/notebook.ipynb>

Share this link with anyone (i.e. colleagues, students) who would like to use
your Binder.

What technology does Binder use?
--------------------------------

Binder combines several open-source technologies, especially:

* `repo2docker <https://repo2docker.readthedocs.org>`_, for quickly generating
  Docker images from a GitHub repository.
* `JupyterHub <https://z2jh.jupyter.org>`_, for connecting a built Docker
  image to cloud computation and a user-facing web portal.
* `BinderHub <https://binderhub.readthedocs.org>`_, for gluing the above two
  tools together to create the Binder experience.
