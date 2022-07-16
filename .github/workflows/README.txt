My most starred repos:
| ⭐️Stars   | 📦Repo    | 📚Description |
| --------- | ----------- | -------------- |
{{ loop 3_MOST_STARRED_REPOS }}
| {{ REPO_STARS }} | [{{ REPO_FULL_NAME }}]({{ REPO_URL }}) | {{ REPO_DESCRIPTION }} |

This is a basic workflow to help you get started with Actions
Controls when the workflow will run
Triggers the workflow on push or pull request events but only for the "main" branch
 Allows you to run this workflow manually from the Actions tab
 A workflow run is made up of one or more jobs that can run sequentially or in parallel
 This workflow contains a single job called "build"
 uses ubuntu build
 Steps represent a sequence of tasks that will be executed as part of the job
  hecks-out your repository under $GITHUB_WORKSPACE, so your job can access it
 Runs a single command using the runners shell
  Runs a set of commands using the runners shell
  Checkout the branch
  do some operation that changes a file in the git repo
  setup the username and email. I tend to use 'GitHub Actions Bot' with no email by default
