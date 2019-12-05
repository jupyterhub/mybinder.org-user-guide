# Sample Binder Repositories


Below we list several sample Binder repositories that
demonstrate how to compose build files in order to create
Binders with varying environments. You can find all of the
repositories listed on this page at the
[binder-examples GitHub organization](https://github.com/binder-examples).


## Managing languages


---------
### Python environment with requirements.txt

[![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/binder-examples/requirements/master) | [repo link](https://github.com/binder-examples/requirements)

A Binder-compatible repo with a `requirements.txt` file.

Access this Binder at the following URL: 

http://mybinder.org/v2/gh/binder-examples/requirements/master

#### Notes
The `requirements.txt` file should list all Python libraries that your notebooks
depend on, and they will be installed using:

```
pip install -r requirements.txt
```

The base Binder image contains no extra dependencies, so be as
explicit as possible in defining the packages that you need. This includes
specifying explicit versions wherever possible.

In this example we include the library `seaborn` which will be installed in
the environment, and our notebook uses it to plot a figure.

#### Files in this repository
```
index.ipynb
requirements.txt
```
```eval_rst
|
|

```
---------
### Conda environment with environment.yml

[![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/binder-examples/conda_environment/v1.0?filepath=index.ipynb) | [repo link](https://github.com/binder-examples/conda)

A Binder-compatible repo with an `environment.yml` file.

Access this Binder at the following URL:

http://mybinder.org/v2/gh/binder-examples/conda_environment/v1.0?filepath=index.ipynb

#### Notes
The `environment.yml` file should list all Python libraries on which your notebooks
depend, specified as though they were created using the following `conda` commands:

```
source activate example-environment
conda env export > environment.yml
```

Note that the only libraries available to you will be the ones specified in
the `environment.yml`, so be sure to include everything that you need!

#### Files in this repository
```
environment.yml
index.ipynb
```
```eval_rst
|
|

```
---------
### python package with setup.py

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/binder-examples/setup.py/master?filepath=example_notebook%2Fimport_mypackage.ipynb) | [repo link](https://github.com/binder-examples/setup.py)

A Binder-compatible repo with a python package and a `setup.py` file.


#### Notes

It is convenient to provide an [example Jupyter notebook ](https://github.com/binder-examples/setup.py/blob/master/example_notebook/import_mypackage.ipynb) for a new package and add the hooks necessary to run the example with Binder. However, normally the package will not be included in the python path. To do that, one needs a `setup.py` for the package (see [binder docs](https://mybinder.readthedocs.io/en/latest/using.html#setup-py)). Once this is done, it is possible to import the package in a notebook running within Binder. 

This setup.py was originally adapted from [https://github.com/kennethreitz/setup.py](https://github.com/kennethreitz/setup.py) by @cranmer

#### Files in this repository
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
### Julia and Python environments

[![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/binder-examples/julia_python/master) | [repo link](https://github.com/binder-examples/julia-python)

This example shows how you can install a Julia and Python environment side-by-side.
In this repository are *both* an `environment.yml` file as well as a `REQURE` file.
The former corresponds to an anaconda python environment, and the latter corresponds
to a Julia environment. Both kernels will be available to you in a built Binder
environment.

#### Files in this repository
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
### Julia Binder demo

This is a demo of Julia functionality for the Binder project. Simply
go to the URL below and it will launch an interactive Julia environment:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/binder-examples/demo-julia/master?filepath=demo.ipynb) | [repo link](https://github.com/binder-examples/demo-julia)


#### Files in this repository
```
REQUIRE
demo.ipynb
```
```eval_rst
|
|

```
---------
### Specifying an R environment with a runtime.txt file

Jupyter+R: [![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/binder-examples/r/master?filepath=index.ipynb)

RStudio: [![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/binder-examples/r/master?urlpath=rstudio)

RShiny: [![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/binder-examples/r/master?urlpath=shiny/bus-dashboard/)

Binder supports using R and RStudio, with libraries pinned to a specific
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

#### Files in this repository
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
### Specifying an R environment by having a DESCRIPTION file

Jupyter+R: [![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/binder-examples/binder-r-description/master?filepath=test-library.ipynb)

RStudio: [![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/binder-examples/binder-r-description/master?urlpath=rstudio)


Binder supports using R and RStudio, with libraries pinned to a specific
snapshot on [MRAN](https://mran.microsoft.com/documents/rro/reproducibility).

If you specify a `runtime.txt` file that is formatted like:

```
r-<YYYY>-<MM>-<DD>
```

where YYYY-MM-DD it will use the MRAN snapshot of that day for setting up the R runtime.

Without specifying a `runtime.txt` it will use a 2-day old snapshot of MRAN.

Both [RStudio](https://www.rstudio.com/) and [IRKernel](https://irkernel.github.io/)
are installed by default, so you can use either the Jupyter notebook interface or
the RStudio interface.

#### Files in this repository
```
DESCRIPTION
NAMESPACE
R
test-library.ipynb
```
```eval_rst
|
|

```
---------
### Octave on mybinder.org

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/binder-examples/octave/master?filepath=index.ipynb) | [repo link](https://github.com/binder-examples/octave)

An example of using Octave on [mybinder.org](https://mybinder.org/).

This shows you how to make Matlab code that works with [Octave](https://www.gnu.org/software/octave/) run on [mybinder.org](https://mybinder.org/).

The [example notebook](index.ipynb) is taken from the [octave_kernel](https://github.com/Calysto/octave_kernel) repository.

#### Files in this repository
```
apt.txt
environment.yml
index.ipynb
```
```eval_rst
|
|

```
## User interfaces


---------
### JupyterLab + Binder

[![Binder](http://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/binder-examples/jupyterlab/master?urlpath=lab/tree/index.ipynb) | [repo link](https://github.com/binder-examples/jupyterlab)

JupyterLab is packaged with Binder repositories by default. In order to
run a JupyterLab session, you have two options:

#### Start JupyterLab after you start your Binder

Do the following:

1. Launch a Binder instance (e.g., by clicking the Binder badge)
2. Replace `tree` at the end of your URL with `lab`.
3. That's it!

#### Create a Binder link that points to JupyterLab

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
 

#### Files in this repository
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
### Enabling Jupyter Extensions with post-build commands

[![Binder](https://mybinder.org/badge_logo.svg)](https://beta.mybinder.org/v2/gh/binder-examples/jupyter-extension/master?filepath=index.ipynb) (Jupyter Notebook) | [repo link](https://github.com/binder-examples/jupyter-extension)  
[![Binder](https://mybinder.org/badge_logo.svg)](https://beta.mybinder.org/v2/gh/binder-examples/jupyter-extension/master?urlpath=lab) (Jupyter Lab) | [repo link](https://github.com/binder-examples/jupyter-extension) 

This example demonstrates how to enable Jupyter extensions with Binder.We currently only cover one example
in this repo. Be aware that some are idiosyncratic in how they're enabled.

We accomplish each step using a `requirements.txt` file to install the extension,
then a `postBuild` file to enable it.

#### ipywidgets

Ipywidgets lets you create interactive widgets in your notebook.
Installation is fairly straightforward. You install the python package,
then enable the extension.

The postBuild file defines commands (one per line) to be run with bash.
In this case, we first enable the ipywidgets extension in the classic notebook interface. We then use it to install a Jupyter Lab extension
(by calling jupyter labextension) which allows ipywidgets
to be displayed within notebooks.

#### Files in this repository
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
### Creating interactive presentations on Binder with RISE

[![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/binder-examples/jupyter-rise/master?filepath=index.ipynb) | [repo link](https://github.com/binder-examples/jupyter-rise)

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

#### Files in this repository
```
environment.yml
index.ipynb
```
```eval_rst
|
|

```
---------
### Interactive apps from Jupyter Notebooks

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/binder-examples/appmode/master?urlpath=apps%2Findex.ipynb) | [repo link](https://github.com/binder-examples/appmode)

This repository demonstrates how to create interactive webapps from a Jupyter Notebook.
This is similar to how Shiny apps work in R.

Using the `appmode` Jupyter plugin, a notebook's code will be run, and then only the markdown cells and
code outputs will be shown.

You can check out the `appmode` repository here: https://github.com/oschuett/appmode

#### Files in this repository
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
### Running a bokeh server with Binder

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/binder-examples/bokeh/master?urlpath=/proxy/5006/bokeh-app) | [repo link](https://github.com/binder-examples/bokeh)

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
#### Files in this repository
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
### stencila-py

Demo for Stencila &amp; DAR on binder with [Python](https://www.python.org/) code.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/binder-examples/stencila-py/master?urlpath=stencila) | [repo link](https://github.com/binder-examples/stencila-py)

Learn more about [Stencila](https://stenci.la/) and its integration with [Binder](https://mybinder.org/) in this [blog post](https://elifesciences.org/labs/d42fe2b9/integrating-binder-and-stencila-the-building-blocks-to-increased-open-communication-and-transparency).

#### Files in this repository
```
article
```
```eval_rst
|
|

```
## System environments


---------
### Specifying a Python 2 environment with `runtime.txt`

[![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/binder-examples/python2_runtime/master) | [repo link](https://github.com/binder-examples/python2_runtime)

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

#### Files in this repository
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
### Mixing Python 2 and 3 kernels with `runtime.txt`

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/binder-examples/python2_with_3/master) | [repo link](https://github.com/binder-examples/python2_with_3)

Sometimes you want *both* Python 2 and Python 3 (e.g., if you have a mixture of notebooks that use each
version of the language). This repository demonstrates how to handle these cases with `repo2docker`. You can
specify a Python 2.7 environment with the `runtime.txt` file. In this case, `repo2docker` will install Python 2
*alongside* Python 3 (though all commands will default to Python 2). In this case, you can install Python 3 dependencies
with `requirements3.txt`, while a file called `requirements.txt` alone will install to the Python 2 environment.
#### Files in this repository
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
### Using latex with Binder

[![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/binder-examples/latex/master?filepath=index.ipynb) | [repo link](https://github.com/binder-examples/latex)

This repository demonstrates how to install latex alongside matplotlib
for Binder. This repository also makes use of [JupyterLab Latex](https://github.com/jupyterlab/jupyterlab-latex) to render latex files in Jupyter lab. This requires a few different build components:

* `apt.txt` for apt-installing the latex components
* `environment.yml` for installing the python dependencies
* `postBuild` for forcing matplotlib to build the font cache and for installing JupyterLab Latex.

Thanks to [m-weigand](https://github.com/m-weigand) for giving
[inspiration for this repo](https://github.com/m-weigand/binder-example-latex-mpl/blob/master/index.ipynb)!

#### Files in this repository
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
### Installing packages from `apt` repositories

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/binder-examples/apt_install/master?filepath=index.ipynb) | [repo link](https://github.com/binder-examples/apt_install)

Sometimes you want packages that exist outside of the language-specific packaging
ecosystems of Python/R/Julia. Binder makes it possible to `apt-install` packages
from the ubuntu apt repository. This repository demonstrates how to do this by specifying
names in an `apt.txt` file.
#### Files in this repository
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
### Multi-language demo.

This is a demo showing how you can intermingle Python,  R, Rust, Fortran, Cython, C. 

You can try it :

[![Binder](http://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/binder-examples/multi-language-demo/master) | [repo link](https://github.com/binder-examples/multi-language-demo)

And read the [accompanying blog post](https://blog.jupyter.org/i-python-you-r-we-julia-baf064ca1fb6).


#### Files in this repository
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
### Using conda with pip in the same build

[![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/binder-examples/python-conda_pip/master?filepath=index.ipynb) | [repo link](https://github.com/binder-examples/python-conda_pip)

If you use `environment.yml`, then Binder will use a Miniconda distribution
to install your packages. However, you may still want to use `pip`. In
this case, you should **not** use a `requirements.txt` file, but instead use
a `- pip` section in `environment.yml`. This repository is an example of how
to construct your `environment.yml` file to accomplish this.

#### Files in this repository
```
environment.yml
index.ipynb
```
```eval_rst
|
|

```
## Data and reproducibility


---------
### Remote Storage with Binder

[![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/binder-examples/remote_storage/master) | [repo link](https://github.com/binder-examples/remote_storage)

A Binder-compatible repo that shows accessing data from remote sources.

Access this Binder at the following URL:

http://mybinder.org/v2/gh/binder-examples/remote_storage/master


#### Notes
The notebooks use `boto` and `requests` to load both images and tables from S3.
The image loading makes use of `PIL` and the table loading
makes use of `pandas`.

#### Files in this repository
```
index.ipynb
requirements.txt
```
```eval_rst
|
|

```
---------
### Importing data with Quilt

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/binder-examples/data-quilt/master?filepath=index.ipynb) | [repo link](https://github.com/binder-examples/data-quilt)

#### Pull data into Binder notebooks
This example uses [Quilt](http://quiltdata.com) to inject data packages into a Jupyter notebook.

Data packages are versioned, immutable snapshots of data. Data packages may contain data of any size. Here is an example of data package: [uciml/iris](https://quiltdata.com/package/uciml/iris).

#### How to specify data dependencies in your own Binder

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
###!/bin/bash
quilt install
```
If you are adopting the `binder` folder pattern for your repo2docker configuration files, and including `quilt.yml`, your postBuild file should look like this:

```bash
###!/bin/bash
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
    
#### Developer

* [Quilt repository](https://github.com/quiltdata/quilt)
* [Quilt docs](https://docs.quiltdata.com)

#### Files in this repository
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
### [Nixpkgs](https://github.com/nixos/nixpkgs) BinderHub example

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/binder-examples/nix/master) | [repo link](https://github.com/binder-examples/nix)

### Why Nix?

[Nix](https://github.com/nixos/nixpkgs) would be a great addition to reproducible data science. It is a unique package manager. Some notable features:

 - 100% reproducible environments (pin to exact commit in repository)
 - both a source and binary package repository
 - allows customized compilation and version of every package
 - can run identical environment outside of docker (all linux distros + dawin)
 - as of now [45,000+ packages](https://repology.org/repositories/statistics/total)
 - fully declarative environments
 - packages: python, javascript, julia, R, haskell, perl, and many other languages (some better than others).

Assuming that you have [`nix`
installed](https://nixos.org/nix/download.html) (compatible with all
linux distributions and darwin (Mac OS)) you can run this repository
locally (no need for binderhub). It will be identical assuming you
have pinned repositories. Nix can coexist fine with other package
managers.

This derivation installs `python37`, `numpy`, and `scipy`.

For a more detailed example see the detailed [binderhub example costrouc/nix-binder-example](https://github.com/costrouc/nix-binder-example)

#### Files in this repository
```
LICENSE.md
default.nix
nix-introduction.ipynb
```
```eval_rst
|
|

```
## Dockerfile environments


---------
### Minimal Dockerfiles for Binder

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/binder-examples/minimal-dockerfile/master) | [repo link](https://github.com/binder-examples/minimal-dockerfile)

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

which you can try out: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/binder-examples/minimal-dockerfile/truly-minimal)

However, it would be better to consume the NB_UID/NB_USER arguments and create a real user:

```docker
### create user with a home directory
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

#### Files in this repository
```
Dockerfile
```
```eval_rst
|
|

```
---------
### Using a Docker image from the Jupyter `docker-stacks` repository

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/binder-examples/jupyter-stacks/master) | [repo link](https://github.com/binder-examples/jupyter-stacks)

Sometimes you just want to inherit from one of the pre-built images
maintained by the Jupyter Project's [Docker Stacks](https://github.com/jupyter/docker-stacks),
and perhaps add just an extra library or two. This example shows you how
to do that - check out the Dockerfile.

Note that in this case we are using a docker image that already satisfies
the [criteria](http://mybinder.readthedocs.io/en/latest/dockerfile.html#preparing-your-dockerfile)
for use on binder, we don't need to install notebook or anything manually.

#### Files in this repository
```
Dockerfile
```
```eval_rst
|
|

```
---------
### Specifying an R environment with a runtime.txt file

Jupyter+R: [![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/binder-examples/rocker/master?filepath=index.ipynb)

RStudio: [![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/binder-examples/rocker/master?urlpath=rstudio)

RShiny: [![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/binder-examples/rocker/master?urlpath=shiny/bus-dashboard/)

Both [RStudio](https://www.rstudio.com/) and [IRKernel](https://irkernel.github.io/)
are installed by default, so you can use either the Jupyter notebook interface or
the RStudio interface.

This repository also contains an example of a Shiny app.

#### Files in this repository
```
Dockerfile
bus-dashboard
index.ipynb
install.R
```
```eval_rst
|
|

```
