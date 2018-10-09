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
## Python packages with setup.py

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/binder-examples/setup.py/master?filepath=example_notebook%2Fimport_mypackage.ipynb)

A Binder-compatible repo with a python package and a `setup.py` file.

Access this binder at the following URL:

https://mybinder.org/v2/gh/binder-examples/setup.py/master?filepath=example_notebook%2Fimport_mypackage.ipynb

### Notes
This repository demonstrates how to install a python package with setup.py 

### Files in this repository
```
LICENSE
MANIFEST.in
README.md
setup.py
mypackage/__init__.py
mypackage/__version__.py
mypackage/core.py
example_notebook/import_mypackage.ipynb

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

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/v2/gh/binder-examples/latex/master?filepath=index.ipynb) | [repo link](https://github.com/binder-examples/latex)

This repository demonstrates how to install latex alongside matplotlib
for Binder. This repository also makes use of [JupyterLab Latex](https://github.com/jupyterlab/jupyterlab-latex) to render latex files in Jupyter lab. This requires a few different build components:

* `apt.txt` for apt-installing the latex components
* `environment.yml` for installing the python dependencies
* `postBuild` for forcing matplotlib to build the font cache and for installing JupyterLab Latex.

Thanks to [m-weigand](https://github.com/m-weigand) for giving
[inspiration for this repo](https://github.com/m-weigand/binder-example-latex-mpl/blob/master/index.ipynb)!

### Files in this repository
```
apt.txt
environment.yml
index.ipynb
postBuild
sample.tex
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

Jupyter+R: [![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/v2/gh/binder-examples/r/master?filepath=index.ipynb)

RStudio: [![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/v2/gh/binder-examples/r/master?urlpath=rstudio)

RShiny: [![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/v2/gh/binder-examples/r/master?urlpath=shiny/bus-dashboard/)

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

This repository also contains an example of a Shiny app.

### Files in this repository
```
bus-dashboard
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

2. Specify data package dependencies in `quilt.yml` ([docs](https://docs.quiltdata.com/api/api-cli)). For example:

```
packages:
  - vgauthier/DynamicPopEstimate   # get the latest version
  - danWebster/sgRNAs:a972d92      # get a specific hash (short hash)
  - akarve/sales:tag:latest        # get a specific tag
  - asah/snli:v:1.0                # get a specific version
```

3. Include the following lines at the top of `postBuild`. (`postBuild` should be executable: `chmod +x postBuild` on UNIX, `git update-index --chmod=+x postBuild` for Windows).

```bash
##!/bin/bash
quilt install
```
If you are adopting the `binder` folder pattern for your repo2docker configuration files, and including `quilt.yml`, your postBuild file should look like this:

```bash
##!/bin/bash
quilt install @./binder/quilt.yml
```
More info about how to install data packages via the `quilt install` command is available [here](https://docs.quiltdata.com/api/api-cli#quilt-install-file-quilt-yml).
    
4. Now you can access the package data in your Jupyter notebooks:

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
---------
## Multi-language demo.

This is a demo showing how you can intermingle Python,  R, Rust, Fortran, Cython, C. 

You can try it :

[![Binder](http://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/binder-examples/multi-language-demo/master) | [repo link](https://github.com/binder-examples/multi-language-demo)

And read the [accompanying blog post](https://blog.jupyter.org/i-python-you-r-we-julia-baf064ca1fb6).


### Files in this repository
```
23-Cross-Language-Integration.ipynb
REQUIRE
apt.txt
data.csv
environment.yml
julia.ipynb
polyglot-ds-prep.ipynb
polyglot-ds.ipynb
postBuild
```
```eval_rst
|
|

```
---------
## continuous-build

This is the continuous build repository, with example configurations (and a basic 
one set up to run on CircleCI) to show how you can use repo2docker to build
a container that serves your notebook for others to use.

### Documentation

You will generally want to copy the `.circleci` folder and its contents to your own folder
with some corresponding notebook and requirements file. For complete documentation, please see 
[repo2docker](https://repo2docker.readthedocs.io/en/latest/deploy.html) 
on ReadTheDocs.

### Examples Provided

Included in this example are:

 - [.circleci](.circleci): a hidden folder that contains the default configuration to build->deploy.
 - [example.ipynb](example.ipynb): an example ipython notebook that will be built in continuous integration
 - [requirements.txt](requirements.txt) an example requirements.txt file for the example notebook.

The circle configuration will be automatically detected in a hidden folder ([.circleci](.circleci))
that has a config.yml inside. In this repository, we have such a folder, and
this can be considered the base template for you to work from.

### Request an Example
We will be adding other example templates here as they are requested. For example,
it would be useful to have further testing of the container, or conversion with nbconvert.
These functions are not provided by default in the configuration above as they may not
be desired for all users. 

If you want to get help, or request an example, please [let us know!](https://www.github.com/binder-examples/continuous-build/issues)

### Files in this repository
```
.circleci
example.ipynb
requirements.txt
```
```eval_rst
|
|

```
---------
## How to get data into your Binder

This example demonstrates a few ways to get data into your binder.


### Small public data

The simplest approach for small data files that are public is to add them directly to your GitHub repository. This way they are directly baked into the environment and versioned together with your code.

Works well for files with sizes up to maybe 10MB.

An example of this is `data/gapminder_all.csv`


### Medium public files

For medium sized files, a few 10s of megabytes to a few hundred megabytes, you can add a special file named `postBuild` to your repository. This will let you fetch the data when the container is built. It increases the image size but means users don't have to download the dataset each time they start the binder. And you know it will always be the same data, even if the source becomes unavailable.

More details on [the `postBuild` file](http://repo2docker.readthedocs.io/en/latest/config_files.html#postbuild).

#### How to do it
Go to your GitHub repository and create a file called `postBuild`. In your
`postBuild` add the following line:

```
wget -q -O bikes-2016.csv "https://data.stadt-zuerich.ch/dataset/verkehrszaehlungen_werte_fussgaenger_velo/resource/ed354dde-c0f9-43b3-b05b-08c5f4c3f65a/download/2016verkehrszaehlungenwertefussgaengervelo.csv"
```

This will download a dataset measuring cycling and walking activity in the city of Zurich
in the year 2016.

Other methods for fetching data files will also work. We used `wget` because it
is a well known tool, no other reason.


### Large public files

For large files it is not practical to place them in your GitHub repository nor to include them directly in the container image.

> Note: We can't use technical measures to stop you from including very large files in your image. However large images take longer to launch, as well as taking up storage space that mybinder.org has to pay for. Please be considerate.

The best option for large files is to use a library specific to the data format to stream the data as you are using it. An alternative is to download each file on demand as part of your code, this way we only create network traffic when it is really needed.

There are a few restrictions on outgoing traffic from your Binder that are imposed by the team operating https://mybinder.org. Currently only connections to HTTP and Git are allowed. This comes up when people want to use FTP sites to fetch data. For security reasons FTP will never be allowed on https://mybinder.org.

> Note: to start a discussion of opening additional ports create a new issue on the [mybinder.org repository](https://github.com/jupyterhub/mybinder.org-deploy/).

#### How to do it

This really depends on your data format and libraries that support accessing it
over a network. An example of accessing Sentinel 2 images that are several gigabyte
in size is in [`Sentinel2.ipynb`](Sentinel2.ipynb).


### Private files

There currently is no way to access files which are not public from https://mybinder.org.

For security reasons you should consider all information in a Binder as public.
This means:
* there should be no secrets (passwords, tokens, keys, etc) in your
GitHub repository
* you should not type passwords into a running Binder on mybinder.org
* you should not upload your private SSH key or API token to a running Binder

To support access to private files you will have to create a local deployment
of [BinderHub](https://binderhub.readthedocs.io/) where you can then decide
on the security trade offs yourself.


## Contributing and other examples

If you know of other examples for the large files section please contribute them
to this repository. If you find a mistake in this repository feel free to open
an issue or directly contribute a fix.

### Files in this repository
```
Sentinel2.ipynb
data
postBuild
requirements.txt
```
```eval_rst
|
|

```
---------
## Running a bokeh server with Binder

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/binder-examples/bokeh/master?urlpath=/proxy/5006/bokeh-app) | [repo link](https://github.com/binder-examples/bokeh)

This repository demonstrates how to run a Bokeh server from within Binder. To do so, we did the following things:

1. Created a `bokeh-app` directory in the repo with a `main.py` file in it. This is the application that will be served. We've added the
   [Bokeh weather example](https://github.com/bokeh/bokeh/tree/master/examples/app/weather) as a demo. 
2. Installed `bokeh` for the viz and `nbserverproxy` which we'll use to direct people to the port on which Bokeh runs. See `environment.yml`.
3. Added a custom server extension (`bokehserverextension.py`) that will be run to direct people to the Bokeh app (which is run on a port)
4. Used `postBuild` to enable the `nbserverproxy` extension, then set up and enable our custom server extension for Bokeh. 
5. Created a Binder link that uses `urlpath` to point users to the port on which the Bokeh server will run:

   ```
   https://mybinder.org/v2/gh/binder-examples/bokeh/master?urlpath=/proxy/5006/bokeh-app
   ```
   
When people click on the Binder link, they should be directed to the running Bokeh app.
### Files in this repository
```
bokeh-app
bokehserverextension.py
environment.yml
postBuild
```
```eval_rst
|
|

```
---------
## Octave on mybinder.org

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/binder-examples/octave/master?filepath=index.ipynb) | [repo link](https://github.com/binder-examples/octave)

An example of using Octave on [mybinder.org](https://mybinder.org/).

This shows you how to make Matlab code that works with [Octave](https://www.gnu.org/software/octave/) run on [mybinder.org](https://mybinder.org/).

The [example notebook](index.ipynb) is taken from the [octave_kernel](https://github.com/Calysto/octave_kernel) repository.

### Files in this repository
```
apt.txt
environment.yml
index.ipynb
```
```eval_rst
|
|

```
---------
## python package with setup.py

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/binder-examples/setup.py/master?filepath=example_notebook%2Fimport_mypackage.ipynb) | [repo link](https://github.com/binder-examples/setup.py)

A Binder-compatible repo with a python package and a `setup.py` file.

Access this binder at the following URL:

https://mybinder.org/v2/gh/cranmer/setup.py/master?filepath=example_notebook%2Fimport_mypackage.ipynb

### Notes

It is convenient to provide an [example Jupyter notebook ](example_notebook/import_mypackage.ipynb) for a new package and add the hooks necessary to run the example with Binder. However, normally the package will not be included in the python path. To do that, one needs a `setup.py` for the package (see [binder docs](https://mybinder.readthedocs.io/en/latest/using.html#setup-py)). Once this is done, it is possible to import the package in a notebook running within Binder. 

This setup.py was originally adapted from https://github.com/kennethreitz/setup.py by @cranmer

### Files in this repository
```
MANIFEST.in
example_notebook
mypackage
setup.py
```
```eval_rst
|
|

```
---------
## Minimal Dockerfiles for Binder

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/binder-examples/minimal-dockerfile/master) | [repo link](https://github.com/binder-examples/minimal-dockerfile)

[Binder](https://mybinder.org) needs only one thing for images to work:

- to be able to launch `jupyter notebook` as a specified user (passed via docker build args as NB_UID/NB_USER)

What this means in practice is that the `notebook` package must be installed and on PATH:

```docker
RUN pip install --no-cache notebook
```

That's *almost* everything.

The remaining piece is that the specified user must be able to *start* the notebook,
which requires certain permissions like being able to write to the home directory.

The absolute bare minimum for this is to set HOME to `/tmp` so that it's writable,
which would make the shortest, smallest Dockerfile that works on Binder:

```docker
FROM python:3.7-slim
RUN pip install --no-cache notebook
ENV HOME=/tmp
```

which you can try out: [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/binder-examples/minimal-dockerfile/truly-minimal)

However, it would be better to consume the NB_UID/NB_USER arguments and create a real user:

```docker
## create user with a home directory
ARG NB_USER
ARG NB_UID
ENV USER ${NB_USER}
ENV HOME /home/${NB_USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}
WORKDIR ${HOME}
```

From this point, you can start adding files, installing packages, etc.

### Files in this repository
```
Dockerfile
```
```eval_rst
|
|

```
