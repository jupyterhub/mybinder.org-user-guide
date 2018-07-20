# Sample Binder Repositories


Below we list several sample Binder repositories that
demonstrate how to compose build files in order to create
Binders with varying environments. You can find all of the
repositories listed on this page at the
[binder-examples GitHub organization](https://github.com/binder-examples).


---------
## Julia and Python environments

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/v2/gh/binder-examples/julia_python/master) | [repo link](https://github.com/binder-examples/julia-python)

This example shows how you can install a Julia and Python environment side-by-side.
In this repository are *both* an `environment.yml` file as well as a `REQURE` file.
The former corresponds to an anaconda python environment, and the latter corresponds
to a Julia environment. Both kernels will be available to you in a built Binder
environment.

### Files in this repository
```
REQUIRE
environment.yml
julia.ipynb
python-and-julia.ipynb
python.ipynb
```
```eval_rst
|
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

### Files in this repository
```
index.ipynb
requirements.txt
```
```eval_rst
|
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

### Files in this repository
```
environment.yml
index.ipynb
```
```eval_rst
|
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

### Files in this repository
```
index.ipynb
requirements.txt
```
```eval_rst
|
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

Thanks to [m-weigand](https://github.com/m-weigand) for giving
[inspiration for this repo](https://github.com/m-weigand/binder-example-latex-mpl/blob/master/index.ipynb)!

### Files in this repository
```
apt.txt
index.ipynb
postBuild
requirements.txt
```
```eval_rst
|
|

```
---------
## JupyterLab + Binder

[![Binder](http://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/binder-examples/jupyterlab/master?urlpath=lab/tree/index.ipynb) | [repo link](https://github.com/binder-examples/jupyterlab)

JupyterLab is packaged with Binder repositories by default. In order to
run a JupyterLab session, you have two options:

### Start JupyterLab after you start your Binder

Do the following:

1. Launch a Binder instance (e.g., by clicking the Binder badge)
2. Replace `tree` at the end of your URL with `lab`.
3. That's it!

### Create a Binder link that points to JupyterLab

You can also create a Binder link that points to JupyterLab by adding the following
to the end of your link:

`?urlpath=lab`

You can point to a specific file using JupterLab by including a file path
beginning with `tree/` to the end of `urlpath`, like so:

`?urlpath=lab/tree/path/to/my/notebook.ipynb`

For example, the Binder badge above goes to the following URL:

`http://mybinder.org/v2/gh/binder-examples/jupyterlab/master?urlpath=lab/tree/index.ipynb`

Note: this repository also installs several JupyterLab extensions via a `postBuild` script, allowing
you to use JupyterLab's extensions and widgets functionality.

For a more complete demo of JupyterLab using Binder, see the
[JupyterLab Demo](https://github.com/jupyterlab/jupyterlab-demo).

### Files in this repository
```
.profile
.test
.tmp
binder
geojson-extension.geojson
index.ipynb
```
```eval_rst
|
|

```
---------
## Specifying an R environment with a runtime.txt file

Jupyter+R: [![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/v2/gh/binder-examples/r/master?filepath=index.ipynb) | [repo link](https://github.com/binder-examples/r)

RStudio: [![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/v2/gh/binder-examples/r/master?urlpath=rstudio) | [repo link](https://github.com/binder-examples/r)

Binder supports using R + RStudio, with libraries pinned to a specific 
snapshot on [MRAN](https://mran.microsoft.com/documents/rro/reproducibility).

You need to have a `runtime.txt` file that is formatted like:

```
r-<YYYY>-<MM>-<DD>
```

where YYYY-MM-DD is a snapshot at MRAN that will be used for installing
libraries.

You can also have an `install.R` file that will be executed during build,
and can be used to install libraries.

Both [RStudio](https://www.rstudio.com/) and [IRKernel](https://irkernel.github.io/)
are installed by default, so you can use either the Jupyter notebook interface or
the RStudio interface.

### Files in this repository
```
index.Rmd
index.ipynb
install.R
runtime.txt
```
```eval_rst
|
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

**important:**
Make sure that you save your notebooks with a python 2 kernel activated,
as this defines which kernel Binder will use when a notebook is opened.

**note:**
If you *also* wish to install python 3 dependencies, you may do so
by including a file called `requirements3.txt`. The packages
inside will be installed into the python 3 environment.

### Files in this repository
```
index.ipynb
requirements.txt
runtime.txt
```
```eval_rst
|
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

### Files in this repository
```
index.ipynb
postBuild
requirements.txt
```
```eval_rst
|
|

```
---------
## Using conda with pip in the same build

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/v2/gh/binder-examples/python-conda_pip/master?filepath=index.ipynb) | [repo link](https://github.com/binder-examples/python-conda_pip)

If you use `environment.yml`, then Binder will use a Miniconda distribution
to install your packages. However, you may still want to use `pip`. In
this case, you should **not** use a `requirements.txt` file, but instead use
a `- pip` section in `environment.yml`. This repository is an example of how
to construct your `environment.yml` file to accomplish this.

### Files in this repository
```
environment.yml
index.ipynb
```
```eval_rst
|
|

```
---------
## Creating interactive presentations on Binder with RISE

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/v2/gh/binder-examples/jupyter-rise/master?filepath=index.ipynb) | [repo link](https://github.com/binder-examples/jupyter-rise)

RISE allows you to quickly generate a live, interactive presentation from a
Jupyter Notebook that is connected to the underlying Kernel of the notebook.
Using a new feature for automatically launching
the RISE plugin when a notebook is opened, RISE can be used to share interactive
presentations that run in the cloud with Binder.
This repository demonstrates how to accomplish this.

To make your RISE presentation automatically-launch with it is open,
add an `autolaunch=true` configuration
parameter to a notebook's `livereveal` section in the
metadata. E.g.:

```
...
"livereveal": {
        "autolaunch": true
        }
...
```

When the notebook is launched, your
presentation will automatically begin.

See the [RISE Documentation](https://damianavila.github.io/RISE/)
for more information.

### Files in this repository
```
environment.yml
index.ipynb
```
```eval_rst
|
|

```
---------
## Interactive apps from Jupyter Notebooks

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/binder-examples/appmode/master?urlpath=apps%2Findex.ipynb) | [repo link](https://github.com/binder-examples/appmode)

This repository demonstrates how to create interactive webapps from a Jupyter Notebook.
This is similar to how Shiny apps work in R.

Using the `appmode` Jupyter plugin, a notebook's code will be run, and then only the markdown cells and
code outputs will be shown.

You can check out the `appmode` repository here: https://github.com/oschuett/appmode

### Files in this repository
```
environment.yml
index.ipynb
ipyvolume_demo.ipynb
postBuild
```
```eval_rst
|
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

### Files in this repository
```
Dockerfile
```
```eval_rst
|
|

```
---------
## Mixing Python 2 and 3 kernels with `runtime.txt`

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/binder-examples/python2_with_3/master) | [repo link](https://github.com/binder-examples/python2_with_3)

Sometimes you want *both* Python 2 and Python 3 (e.g., if you have a mixture of notebooks that use each
version of the language). This repository demonstrates how to handle these cases with `repo2docker`. You can
specify a Python 2.7 environment with the `runtime.txt` file. In this case, `repo2docker` will install Python 2
*alongside* Python 3 (though all commands will default to Python 2). In this case, you can install Python 3 dependencies
with `requirements3.txt`, while a file called `requirements.txt` alone will install to the Python 2 environment.
### Files in this repository
```
index2.ipynb
index3.ipynb
requirements.txt
requirements3.txt
runtime.txt
```
```eval_rst
|
|

```
---------
## Installing packages from `apt` repositories

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/binder-examples/apt_install/master?filepath=index.ipynb) | [repo link](https://github.com/binder-examples/apt_install)

Sometimes you want packages that exist outside of the language-specific packaging
ecosystems of Python/R/Julia. Binder makes it possible to `apt-install` packages
from the ubuntu apt repository. This repository demonstrates how to do this by specifying
names in an `apt.txt` file.
### Files in this repository
```
apt.txt
index.ipynb
postBuild
```
```eval_rst
|
|

```
---------
## Importing data with Quilt

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/binder-examples/data-quilt/master?filepath=index.ipynb) | [repo link](https://github.com/binder-examples/data-quilt)

### Pull data into Binder notebooks
This example uses [Quilt](http://quiltdata.com) to inject data packages into a Jupyter notebook.

Data packages are versioned, immutable snapshots of data. Data packages may contain data of any size. Here is an example of data package: [uciml/iris](https://quiltdata.com/package/uciml/iris).

### How to specify data dependencies in your own Binder

1. Add `quilt` to `requirements.txt`

2. Specify data package dependencies in `quilt.yml` ([docs](https://docs.quiltdata.com/cli.html)). For example:

```
packages:
  - vgauthier/DynamicPopEstimate   # get the latest version
  - danWebster/sgRNAs:a972d92      # get a specific hash (short hash)
  - akarve/sales:tag:latest        # get a specific tag
  - asah/snli:v:1.0                # get a specific version
```

3. Include the following lines at the top of `postBuild`. (`postBuild` should be executable: `chmod +x postBuild` on UNIX, `git update-index --chmod=+x postBuild` for Windows).

``` bash
##!/bin/bash
quilt install
```
    
Now you can access the package data in your Jupyter notebooks:

```
In [1]: from quilt.data.akarve import sales
In [2]: sales.transactions()
Out[2]: 
      Row ID  Order ID Order Date Order Priority  Order Quantity       Sales  \
0          1         3 2010-10-13            Low               6    261.5400   
1         49       293 2012-10-01           High              49  10123.0200   
2         50       293 2012-10-01           High              27    244.5700   
...
```
    
### Developer

* [Quilt repository](https://github.com/quiltdata/quilt)
* [Quilt docs](https://docs.quiltdata.com)

### Files in this repository
```
index.ipynb
postBuild
quilt.yml
requirements.txt
```
```eval_rst
|
|

```
