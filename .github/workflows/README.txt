My most starred repos:
| ⭐️Stars   | 📦Repo    | 📚Description |
| --------- | ----------- | -------------- |
{{ loop 3_MOST_STARRED_REPOS }}
| {{ REPO_STARS }} | [{{ REPO_FULL_NAME }}]({{ REPO_URL }}) | {{ REPO_DESCRIPTION }} |

This is a basic workflow to help you get started with Actions
Controls when the workflow will run
Triggers the workflow on push or pull request events but only for the "main" branch
