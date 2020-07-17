# Use GitHub Actions to place a MyBinder.org badge on pull requests

You can facilitate review of GitHub pull requests on [mybinder.org](https://mybinder.org) by using [GitHub Actions](https://github.com/features/actions) to place a ![Binder](https://mybinder.org/badge_logo.svg) badge or link on Pull Requests.  Below are several examples of how to accomplish this.

To enable GitHub Actions, you must place .yaml files that define your GitHub Action workflow in the `/.github/workflows/` directory in your repository.

## Example 1: Comment on pull request with a binder badge

_Note: this example will not work on pull requests from forks.  This is to protect repositories from malicious actors.  To trigger a GitHub Action with sufficient permissions to comment on a pull request from a fork, you must trigger the action via another event, such as a comment or a label.  This is demonstrated in Example 2 below._

The below action uses the [github/script](https://github.com/actions/github-script) Action to call the [GitHub API](https://docs.github.com/en/rest/reference/issues#comments) for the purposes of making a comment on a PR that looks like this:

> ![Binder](https://mybinder.org/badge_logo.svg) 👈 Launch a binder notebook on this branch

```yaml
#/.github/workflows/binder-badge.yaml
name: Binder Badge
on: [pull_request]

jobs:
  binder:
    runs-on: ubuntu-latest
    steps: 
    - name: comment on PR with Binder link
      uses: actions/github-script@v1
      with:
        github-token: ${{secrets.GITHUB_TOKEN}}
        script: |
          var BRANCH_NAME = process.env.BRANCH_NAME;
          github.issues.createComment({
            issue_number: context.issue.number,
            owner: context.repo.owner,
            repo: context.repo.repo,
            body: `[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/${context.repo.owner}/${context.repo.repo}/${BRANCH_NAME}) :point_left: Launch a binder notebook on this branch`
          }) 
      env:
        BRANCH_NAME: ${{ github.event.pull_request.head.ref }}
```

## Example 2: Comment with a Binder badge in response to a comment

In the below example, we will trigger GitHub Actions to run after someone comments on a pull request with the command `/binder`, which will trigger Actions to comment on a PR in the same way as Example 1.

```yaml
#./github/workflows/chatops-binder.yaml
name: Chatops Binder
on: [issue_comment] # issues and PRs are equivalent in terms of comments for the GitHub API

jobs:
  trigger-chatops:
    # Make sure the comment is on a PR, and contains the command "/binder"
    if: (github.event.issue.pull_request != null) &&  contains(github.event.comment.body, '/binder')
    runs-on: ubuntu-latest
    steps:
      # Use the GitHub API to: 
      #  (1) Get the branch name of the PR that has been commented on with "/binder" 
      #  (2) make a comment on the PR with the binder badge
    - name: comment on PR with Binder link
      uses: actions/github-script@v1
      with:
        github-token: ${{secrets.GITHUB_TOKEN}}
        script: |
         // Get the branch name
         octokit.pulls.get({
            owner: context.repo.owner,
            repo: context.repo.repo,
            pull_number: context.payload.issue.number
         }).then( (pr) => {

            // use the branch name to make a comment  on the PR with a Binder badge
            var BRANCH_NAME = pr.data.head.ref
            octokit.issues.createComment({
               issue_number: context.payload.issue.number,
               owner: context.repo.owner,
               repo: context.repo.repo,
               body: `[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/${context.repo.owner}/${context.repo.repo}/${BRANCH_NAME}) :point_left: Launch a binder notebook on this branch`
               })
         })

```

## Further Reading:

Please see the official GitHub Actions [documentation](https://docs.github.com/en/actions) for more information.
