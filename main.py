import os
import sys
import json

# https://docs.github.com/en/actions/learn-github-actions/variables

def main():
    #owner_and_repo = os.environ["GITHUB_ACTION_REPOSITORY"]
    #event_name = os.environ["GITHUB_EVENT_NAME"]
    
    with open(os.environ["GITHUB_EVENT_PATH"]) as f:
        event = json.load(f)
    if not event["delete_branch_on_merge"]:
        sys.exit("""
######

"Delete Branches on Merge" must be enabled for gha-stacked to work correctly
See: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-the-automatic-deletion-of-branches

######
""")

    print(os.environ)
    print(event)

    base_ref = os.environ["GITHUB_BASE_REF"]

    branch_prefixes = os.environ["INPUT_STACK-BRANCH-PREFIXES"]
    branch_prefixes = branch_prefixes.split(",")

    for p in branch_prefixes:
        if base_ref.startswith(p):
            sys.exit(f"""
######

Base branch {base_ref} is unmerged, matches prefix {p}

######
""")

    sys.exit(0)

if __name__ == "__main__":
    main()
