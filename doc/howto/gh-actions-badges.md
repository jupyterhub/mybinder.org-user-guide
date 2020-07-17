# Use GitHub Actions to place a MyBinder.org badge on pull requests

You can facilitate review of GitHub pull requests on [mybinder.org](https://mybinder.org) by using [GitHub Actions](https://github.com/features/actions) to place a ![Binder](https://mybinder.org/badge_logo.svg) badge or link on Pull Requests.  Below are several examples of how to accomplish this.

To enable GitHub Actions, you must place .yaml files that define your GitHub Action workflow in the `/.github/workflows/` directory in your repository.

## Example 1: Comment on pull request with a binder badge

```{note}
This example will not work on pull requests from forks.  This is to protect repositories from malicious actors.  To trigger a GitHub Action with sufficient permissions to comment on a pull request from a fork, you must trigger the action via another event, such as a comment or a label.  This is demonstrated in Example 2 below.
```

The below action uses the [github/script](https://github.com/actions/github-script) Action to call the [GitHub API](https://docs.github.com/en/rest/reference/issues#comments) for the purposes of making a comment on a PR that looks like this:

Download the below file: {download}`binder-badge.yaml <./binder-badge.yaml>`

```{literalinclude} ./binder-badge.yaml
---
language: yaml
---
```

## Example 2: Comment with a Binder badge in response to a comment

In the below example, we will trigger GitHub Actions to run after someone comments on a pull request with the command `/binder`, which will trigger Actions to comment on a PR in the same way as Example 1.

Download the below file: {download}`chatops-binder.yaml <./chatops-binder.yaml>`

```{literalinclude} ./chatops-binder.yaml
---
language: yaml
---
```

## Further Reading:

Please see the official GitHub Actions [documentation](https://docs.github.com/en/actions) for more information.
