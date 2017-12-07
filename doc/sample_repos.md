# Sample Binder Repositories


Below we list several sample Binder repositories that
demonstrate how to compose build files in order to create
Binders with varying environments.


---------
## Julia and Python environments

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/v2/gh/binder-examples/julia_python/master) | [repo link](https://github.com/binder-examples/julia-python)

This example shows how you can install a Julia and Python environment side-by-side.
In this repository are *both* an `environment.yml` file as well as a `REQURE` file.
The former corresponds to an anaconda python environment, and the latter corresponds
to a Julia environment. Both kernels will be available to you in a built Binder
environment.

### Files
```
REQUIRE
environment.yml
julia.ipynb
python-and-julia.ipynb
python.ipynb
```
```eval_rst
|

```
---------
## Python environment with requirements.txt

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/v2/gh/binder-examples/requirements/master) | [repo link](https://github.com/binder-examples/requirements)

A Binder-compatible repo with a `requirements.txt` file.

Access this Binder at the following URL: 

http://mybinder.org/v2/gh/binder-examples/requirements/master

### Notes
The `requirements.txt` file should list all Python libraries that your notebooks
depend on, and they will be installed using:

```
pip install -r requirements.txt
```

The base Binder image contains no extra dependencies, so be as
explicit as possible in defining the packages that you need. This includes
specifying explict versions wherever possible.

In this example we include the library `seaborn`, and our notebook uses it
to plot a figure. 

### Files
```
index.ipynb
requirements.txt
```
```eval_rst
|

```
---------
## Conda environment with environment.yml

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/v2/gh/binder-examples/conda_environment/v1.0?filepath=index.ipynb) | [repo link](https://github.com/binder-examples/conda)

A Binder-compatible repo with an `environment.yml` file.

Access this Binder at the following URL:

http://mybinder.org/v2/gh/binder-examples/conda_environment/v1.0?filepath=index.ipynb

### Notes
The `environment.yml` file should list all Python libraries on which your notebooks
depend, specified as though they were created using the following `conda` commands:

```
source activate example-environment
conda env export > environment.yml
```

Note that the only libraries available to you will be the ones specified in
the `environment.yml`, so be sure to include everything that you need!

### Files
```
environment.yml
index.ipynb
```
```eval_rst
|

```
---------
## Remote Storage with Binder

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/v2/gh/binder-examples/remote_storage/master) | [repo link](https://github.com/binder-examples/remote_storage)

A Binder-compatible repo that shows accessing data from remote sources.

Access this Binder at the following URL:

http://mybinder.org/v2/gh/binder-examples/remote_storage/master


### Notes
The notebooks use `boto` and `requests` to load both images and tables from S3.
The image loading makes use of `PIL` and the table loading
makes use of `pandas`.

### Files
```
index.ipynb
requirements.txt
```
```eval_rst
|

```
---------
## Using latex with Binder

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/v2/gh/binder-examples/latex/master) | [repo link](https://github.com/binder-examples/latex)

This repository demonstrates how to install latex alongside matplotlib
for Binder. This requires a few different build components:

* `apt.txt` for apt-installing the latex components
* `requirements.txt` for installing the python dependencies
* `postBuild` for forcing matplotlib to build the font cache

Thanks to @m-weigand for giving
[inspiration for this repo](https://github.com/m-weigand/binder-example-latex-mpl/blob/master/index.ipynb)!

### Files
```
apt.txt
index.ipynb
postBuild
requirements.txt
```
```eval_rst
|

```
---------
## JupyterLab + Binder

[![Binder](http://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/binder-examples/jupyterlab/master?urlpath=lab) | [repo link](https://github.com/binder-examples/jupyterlab)

Demonstrate how to use JupyterLab with Binder.

You can enable JupyterLab for a repository in Binder with the following steps:

1. Install the required JupyterLab extensions (see how it is done in this repository)
2. Configure the "Path to a notebook file" dropdown to "URL" and set the value to `lab`
3. That's it!

### Files
```
binder
geojson-extension.geojson
index.ipynb
```
```eval_rst
|

```
---------
## Specifying an R environment with Binder using a Dockerfile

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/v2/gh/binder-examples/dockerfile-r/master?filepath=index.ipynb) | [repo link](https://github.com/binder-examples/dockerfile-r)

While Python and Julia are the only two languages natively supported with
build files, it's possible to create R Kernels for use with Binder as well.

This repository shows how you can use a Dockerfile to install R and
connect it with Jupyter. This lets you run R code from within the Jupyter Notebooks.

### Files
```
Dockerfile
index.ipynb
```
```eval_rst
|

```
---------
## RStudio in Binder using a Dockerfile

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/v2/gh/binder-examples/dockerfile-rstudio/master) | [repo link](https://github.com/binder-examples/dockerfile-rstudio)

This is a proof-of-concept to deploy a Binder that exposes the
RStudio UI instead of a Jupyter Notebook. It also installs
several packages from the tidyverse, and includes a demo
script to show off functionality.

To start your RStudio session, click on "new", and at the bottom will
be `RStudio Session`. Click that and you're ready to go!

*Special thanks to Ryan Lovett (@ryanlovett) for figuring out
RStudio support with JupyterHub*

### Files
```
Dockerfile
How to Launch RStudio.ipynb
index.R
```
```eval_rst
|

```
---------
## Specifying a Python 2 environment with `runtime.txt`

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/v2/gh/binder-examples/python2_runtime/master) | [repo link](https://github.com/binder-examples/python2_runtime)

We can specify various runtime parameters with a `runtime.txt` file. In this
repository, we demonstrate how to install python 2 with the environment.

If you specify `python-2.7` in `runtime.txt`, then:

* A python3 environment is created & installed (this is what the notebook runs from)
* A python2 environment is created and registered
* The contents of `requirements.txt` are installed into the python2 environment

Note:
* Make sure that you save your notebooks with a python 2 kernel activated,
  as this defines which kernel Binder will use when a notebook is opened.
* If you *also* wish to install python 3 dependencies, you may do so by including a
  file called `requirements3.txt`. The packages inside will be installed into the python 3 environment.

### Files
```
index.ipynb
requirements.txt
runtime.txt
```
```eval_rst
|

```
---------
## Enabling Jupyter Extensions with post-build commands

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/binder-examples/jupyter-extension/master?filepath=index.ipynb) | [repo link](https://github.com/binder-examples/jupyter-extension)

This example demonstrates how to enable Jupyter extensions with Binder. We'll
cover a few in this repo because some are idiosyncratic in how they're enabled.

We accomplish each using a `requirements.txt` file to install the extensions,
then a `postBuild` file to enable them.

### ipywidgets

Ipywidgets lets you create interactive widgets in your notebook.
Installation is fairly straightforward. You install the python package,
then enable the extension.

### python-markdown
The `python-markdown` extension is useful for interweaving computational
cells (e.g., python cells) and markdown cells. As this extension automatically
runs code in the notebook, you need to be sure to "trust" the notebooks in your
`postBuild` script (see the script in this repo for example).

### Files
```
index.ipynb
postBuild
requirements.txt
```
```eval_rst
|

```
---------
## Using anaconda with pip in the same build

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/v2/gh/binder-examples/python-conda_pip/master?filepath=index.ipynb) | [repo link](https://github.com/binder-examples/python-conda_pip)

If you use `environment.yml`, then Binder will use a Miniconda distribution
to install your packages. However, you may still want to use `pip`. In
this case, you should **not** use a `requirements.txt` file, but instead use
a `- pip` section in `environment.yml`. This repository is an example of how
to construct your `environment.yml` file to accomplish this.

Access this Binder at the following URL:

http://mybinder.org/v2/gh/binder-examples/python-conda_pip/master?filepath=index.ipynb

### Files
```
environment.yml
index.ipynb
```
```eval_rst
|

```
---------
## Creating interactive presentations on Binder with RISE

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/v2/gh/binder-examples/jupyter-rise/master?filepath=index.ipynb) | [repo link](https://github.com/binder-examples/jupyter-rise)

In a recent release of RISE, there is support for automatically launching
the RISE plugin when a notebook is opened. This repository demonstrates how
to accomplish this for Binder. The trick is to add an `autolaunch=true` configuration
parameter to a notebook's metadata. Then, when the notebook is launched, your
presentation will automatically begin. E.g.:

```
...
"livereveal": {
        "autolaunch": true
        }
...
```

### Files
```
environment.yml
index.ipynb
```
```eval_rst
|

```
---------
## Creating webapps with Binder

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/binder-examples/appmode/master?urlpath=apps%2Findex.ipynb) | [repo link](https://github.com/binder-examples/appmode)

This repository demonstrates how to create webapps with Binder. This is similar to how Shiny apps work in R.
Using the `appmode` Jupyter plugin, a notebook's code will be run, and then only the markdown cells and
code outputs will be shown.

You can check out the `appmode` repository here: https://github.com/oschuett/appmode

### Files
```
environment.yml
index.ipynb
postBuild
```
```eval_rst
|

```
---------
## Using a Docker image from the Jupyter `docker-stacks` repository

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/binder-examples/jupyter-stacks/master) | [repo link](https://github.com/binder-examples/jupyter-stacks)

Sometimes you just want to inherit from one of the pre-built images
maintained by the Jupyter Project's [Docker Stacks](https://github.com/jupyter/docker-stacks),
and perhaps add just an extra library or two. This example shows you how
to do that - check out the Dockerfile.

Note that in this case we are using a docker image that already satisfies
the [criteria](http://mybinder.readthedocs.io/en/latest/dockerfile.html#preparing-your-dockerfile)
for use on binder, we don't need to install notebook or anything manually.

### Files
```
Dockerfile
```
```eval_rst
|

```
