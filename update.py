import os
import git

def sync_with_github(local_repo_path, github_repo_url, github_branch='master'):
    try:
        # Check if the local repository exists
        if not os.path.isdir(local_repo_path):
            print(f"Local repository '{local_repo_path}' does not exist.")
            return

        # Open the local repository
        repo = git.Repo(local_repo_path)

        # Fetch changes from the remote repository
        origin = repo.remotes.origin
        origin.fetch()

        # Get the current commit hash of the local repository
        local_commit = repo.head.commit

        # Get the latest commit hash from the remote repository
        remote_commit = repo.commit(f"origin/{github_branch}")

        # Check if there are differences between the local and remote repositories
        if local_commit != remote_commit:
            print("Differences found. Pushing changes to the GitHub repository...")

            # Push local changes to the GitHub repository
            repo.git.push("origin", github_branch)

            print("Push successful.")
        else:
            print("Local repository is up-to-date with the GitHub repository.")

    except Exception as e:
        print(f"Error syncing with GitHub: {e}")

if __name__ == "__main__":
    # Set your local repository path and GitHub repository URL
    local_repo_path = "./"
    github_repo_url = "https://github.com/Jaswanth28/APIS.git"
    github_branch = "main"  # Replace with the branch you want to sync with

    # Call the sync function
    sync_with_github(local_repo_path, github_repo_url, github_branch)
