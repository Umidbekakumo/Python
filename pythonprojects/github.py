
import requests, os, pprint
pp = pprint.PrettyPrinter(indent=4)
TOKEN = os.getenv('github_token')

# curl -L \
#   -H "Accept: application/vnd.github+json" \
#   -H "Authorization: Bearer <YOUR-TOKEN>"\
#   -H "X-GitHub-Api-Version: 2022-11-28" \
#   https://api.github.com/orgs/ORG/repos

headers = {"Accept": "application/vnd.github+json", "Authorization": f"Bearer {TOKEN}"}
url = "https://api.github.com/repos/Umidbekakumo/Python"

resp = requests.get(url, headers=headers)
repo_data = resp.json()

print(repo_data['name'])
