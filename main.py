import os
import requests 

def main():
    #owner_and_repo = os.environ["GITHUB_ACTION_REPOSITORY"]
    event_name = os.environ["GITHUB_EVENT_NAME"]

    base_ref = os.environ["GITHUB_BASE_REF"]

    if event_name != "pull_request":
        print(f"Action not run on a pull_request, was {event_name}", file=sys.stderr)

    print("base ref:", base_ref)
    print(os.environ)

"""
    r = requests.get(
        f"https://api.github.com/repos/{owner_and_repo}/pulls/{pull_number}/commits",""
        headers = {
            "Authorization": f"Bearer {auth_token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version", "2022-11-28",
        }
    )
    r.raise_for_status()
    pr_state = r.json()
    print(pr_state)
"""
    
if __name__ == "__main__":
    main()
