# Use GitHub Actions to place a MyBinder.org badge on pull requests

You can facilitate review of GitHub pull requests on [mybinder.org](https://mybinder.org) by using [GitHub Actions](https://github.com/features/actions) to place a ![Binder](https://mybinder.org/badge_logo.svg) badge or link on Pull Requests.  Below are several examples of how to accomplish this.

To enable GitHub Actions, you must place .yaml files that define your GitHub Action workflow in the `/.github/workflows/` directory in your repository.


## Example 1: Comment on pull request with a binder badge

The below action uses the [github/script](https://github.com/actions/github-script) Action to call the [GitHub API](https://docs.github.com/en/rest/reference/issues#comments) for the purposes of making a comment on a PR that looks like this:

> ![Binder](https://mybinder.org/badge_logo.svg) 👈 Launch a binder notebook on this branch for commit xxxxxxx

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

## Permissions

You may want to restrict who can trigger a binder badge to be created by [their association](https://developer.github.com/v4/enum/commentauthorassociation/) with a repository.  When triggering GitHub Actions on an [issue_comment](https://docs.github.com/en/actions/reference/events-that-trigger-workflows#issue_comment) event, you can 
access the association of the person who opened the pull request with the variable `github.event.issue.author_association` and the person commenting on the pull request with `github.event.comment.author_association`. 

```{note}
An `issue_comment` event is triggered when you comment on a pull request.  This is because the GitHub API treats issues and pull requests as the same entity in many places.  This is also why you can access the association of the person who opened the pull request with the `github.event.issue.author_association` when the `issue_comment` event occurs.
```

Similarly, when triggering GitHub Actions on a [pull_request](https://docs.github.com/en/actions/reference/events-that-trigger-workflows#pull_request) event, you can access the association of the person who opened the pull request with the variable `github.event.pull_request.author_association`.

For example, this is how you can conditionally trigger the workflow shown in **Example 1** if the person opening the PR is a `OWNER`, `COLLABORATOR`, `MEMBER`, or `CONTRIBUTOR`:

Download the below file: {download}`binder-badge-permissions.yaml <./binder-badge-permissions.yaml>`

```{literalinclude} ./binder-badge-permissions.yaml
---
language: yaml
---
```

## Further Reading

There are many more ways you can customize your workflows to suit your needs.  Please see the official GitHub Actions [documentation](https://docs.github.com/en/actions) for more information.
