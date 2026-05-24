import requests
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization": f"token {GITHUB_TOKEN}"
}

def get_pr_files(owner, repo, pr_number):

    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/files"

    response = requests.get(url, headers=headers)

    print("GitHub Status:", response.status_code)
    print("GitHub Response:", response.json())

    if response.status_code != 200:
        return {"error": response.json()}

    return response.json()