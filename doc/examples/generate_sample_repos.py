"""This is a helper file to auto-generate the sample
READMEs page for the mybinder documentation. It expects
a couple of environment variables to be set corresponding
to your github username / password, or to an access token
you've created (see below for the proper variable names).

The script grabs some metadata and the README text for
all of the binder-examples repositories, and then constructs
a markdown file that can be served on the mybinder.org
documentation page.
"""

from github import Github
import os
from tqdm import tqdm

EXCLUDE_FILES = ['.gitignore', 'LICENSE', 'README.md']
EXCLUDE_REPOS = ['dockerfile-rstudio', 'zero-to-binder']
path_file = os.path.dirname(os.path.abspath(__file__))

# First create a Github instance:
try:
    g = Github(os.environ['GITHUB_USERNAME'],
            os.environ['GITHUB_PASSWORD'])
    org = g.get_organization('binder-examples')
except:
    g = Github(os.environ['GITHUB_TOKEN'])
    org = g.get_organization('binder-examples')

# These are the repositories we'll display. Break them down by topic since the list is getting long
repos = {'Managing languages': ['requirements', 'conda', 'setup.py', 'julia-python', 'demo-julia', 'r', 'binder-r-description', 'octave'],
         'User interfaces': ['jupyterlab', 'jupyter-extension', 'jupyter-rise', 'appmode', 'bokeh', 'stencila-py'],
         'System environments': ['python2_runtime', 'python2_with_3', 'latex', 'apt_install', 'multi-language-demo', 'python-conda_pip'],
         'Data and reproducibility': ['remote_storage', 'data-quilt', 'nix'],
         'Dockerfile environments': ['minimal-dockerfile', 'jupyter-stacks', 'rocker']}

lines = ['% !!!! PROGRAMMATICALLY GENERATED                       !!!!',
         '% !!!! Run generate_sample_repos.py to update this page !!!!',
         '# Sample Binder Repositories',
         ''
         'Below we list several sample Binder repositories that'
         'demonstrate how to compose build files in order to create'
         'Binders with varying environments. You can find all of the'
         'repositories listed on this page at the'
         '[binder-examples GitHub organization](https://github.com/binder-examples).\n']

for category, repo_list in repos.items():
    print(category)
    lines += ["## {}\n\n".format(category)]
    for reponame in tqdm(repo_list):
        repo = org.get_repo(reponame)

        # Base metadata
        link = repo.url.replace('api.github.com/repos', 'github.com')
        name = repo.name

        # Grab repo contents
        files = repo.get_dir_contents('.')
        file_names = [this_file.name
                    for this_file in files if this_file.name not in EXCLUDE_FILES]
        file_names = ['{}'.format(this_name) for this_name in file_names]

        # Parse readme
        readme = repo.get_contents('README.md')
        readme_text = readme.decoded_content.decode()
        readme_text = readme_text.replace('beta.mybinder.org', 'mybinder.org')
        readme_text = readme_text.replace('badge.svg', 'badge_logo.svg')
        readme_text = readme_text.split('\n')

        # Correct for header lines
        for i_line, line in enumerate(readme_text):
            if line.startswith('#'):
                readme_text[i_line] = '##' + line
            if line.startswith('[![Binder]'):
                readme_text[i_line] = line + f' | [![](https://img.shields.io/github/forks/{repo.full_name}?label=GitHub%20Repo&style=social)]({link})'

        # Append to doc file
        lines += readme_text
        lines.append('#### Files in this repository')
        lines.append('```')
        for this_file in file_names:
            lines.append(this_file)
        lines.append('```')

lines = [ln + '\n' for ln in lines]

with open(os.path.join(path_file, 'sample_repos.md'), 'w') as ff:
    ff.writelines(lines)

print('Finished building docs for {} repos.'.format(len([ii for jj in repos.values() for ii in jj])))
