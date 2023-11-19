import os
import sys

# https://docs.github.com/en/actions/learn-github-actions/variables

def main():
    #owner_and_repo = os.environ["GITHUB_ACTION_REPOSITORY"]
    #event_name = os.environ["GITHUB_EVENT_NAME"]

    base_ref = os.environ["GITHUB_BASE_REF"]

    branch_prefixes = os.environ["INPUT_STACK-BRANCH-PREFIXES"]
    branch_prefixes = branch_prefixes.split(",")

    
    if any(base_ref.startswith(p) for p in branch_prefixes):
        sys.exit(f"Base branch {base_ref} is an unmedged stacked PR, matches prefix in {branch_prefixes}")
    else:
        print(f"Base branch {base_ref} is not a stacked PR branch")
        sys.exit(0)

if __name__ == "__main__":
    main()
