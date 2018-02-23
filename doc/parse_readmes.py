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
EXCLUDE_REPOS = ['dockerfile-rstudio', 'zero-to-binder']

# First create a Github instance:
g = Github(os.environ['GITHUB_USERNAME'],
           os.environ['GITHUB_PASSWORD'])

org = g.get_organization('binder-examples')
repos = list(org.get_repos())
repos = [repo for repo in repos if repo.name not in EXCLUDE_REPOS]

lines = ['# Sample Binder Repositories\n',
         '\n'
         'Below we list several sample Binder repositories that\n'
         'demonstrate how to compose build files in order to create\n'
         'Binders with varying environments. You can find all of the\n'
         'repositories listed on this page at the\n'
         '[binder-examples GitHub organization](https://github.com/binder-examples).\n\n']

for i_repo, repo in enumerate(repos):
    print('{}/{}'.format(i_repo+1, len(repos)))

    # Base metadata
    link = repo.url.replace('api.github.com/repos', 'github.com')
    name = repo.name

    # Grab repo contents
    files = repo.get_dir_contents('.')
    file_names = [this_file.name
                  for this_file in files if this_file.name not in EXCLUDE_FILES]
    file_names = ['{}'.format(this_name) for this_name in file_names]

    # Parse readme
    readme = repo.get_file_contents('README.md')
    readme_text = readme.decoded_content.decode()
    readme_text = readme_text.replace('beta.mybinder.org', 'mybinder.org')
    readme_text = readme_text.split('\n')

    # Correct for header lines
    for i_line, line in enumerate(readme_text):
        if line.startswith('#'):
            readme_text[i_line] = '#' + line
        if line.startswith('[![Binder]'):
            readme_text[i_line] = line + ' | [repo link]({})'.format(link)

    if i_line != 0:
        lines.append('---------')

    # Append to doc file
    lines += readme_text
    lines.append('### Files in this repository')
    lines.append('```')
    for this_file in file_names:
        lines.append(this_file)
    lines.append('```')
    lines.append('```eval_rst\n|\n|\n\n```')

lines = [ln + '\n' for ln in lines]

with open('sample_repos.md', 'w') as ff:
    ff.writelines(lines)

print('Finished building docs for {} repos.'.format(len(repos)))
