"""This is a helper file to auto-generate the sample
READMEs page for the mybinder documentation. It expects
a couple of environment variables to be set corresponding
to your github username / password.

The script grabs some metadata and the README text for
all of the binder-examples repositories, and then constructs
a markdown file that can be served on the mybinder.org
documentation page.
"""

from github import Github
import os

EXCLUDE_FILES = ['.gitignore', 'LICENSE', 'README.md']
# First create a Github instance:
g = Github(os.environ['GITHUB_USERNAME'],
           os.environ['GITHUB_PASSWORD'])

org = g.get_organization('binder-examples')
repos = list(org.get_repos())

lines = ['# Sample Binder Repositories\n',
         '\n'
         'Below we list several sample Binder repositories that\n'
         'demonstrate how to compose build files in order to create\n'
         'Binders with varying environments.\n\n']
for ii, repo in enumerate(repos):
    # Base metadata
    link = repo.url.replace('api.github.com/repos', 'github.com')
    name = repo.name

    # Grab repo contents
    files = repo.get_dir_contents('.')
    file_names = [ii.name for ii in files if ii.name not in EXCLUDE_FILES]
    file_names = ['{}'.format(ii) for ii in file_names]

    # Parse readme
    readme = repo.get_file_contents('README.md')
    readme_text = readme.decoded_content.decode()
    readme_text = readme_text.replace('beta.mybinder.org', 'mybinder.org')
    readme_text = readme_text.split('\n')

    # Correct for header lines
    for ii, line in enumerate(readme_text):
        if line.startswith('#'):
            readme_text[ii] = '#' + line
        if line.startswith('[![Binder]'):
            readme_text[ii] = line + ' | [repo link]({})'.format(link)

    if ii != 0:
        lines.append('---------')

    # Append to doc file
    lines += readme_text
    lines.append('### Files')
    lines.append('```')
    for ifile in file_names:
        lines.append(ifile)
    lines.append('```')
    lines.append('```eval_rst\n|\n\n```')

lines = [ln + '\n' for ln in lines]

with open('sample_repos.md', 'w') as ff:
    ff.writelines(lines)
