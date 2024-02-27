import subprocess

def revert_last_commit():
    try:
        # Get the hash of the last commit
        commit_hash = subprocess.check_output(['git', 'log', '--format=%H', '-n', '1']).decode('utf-8').strip()

        # Revert the last commit without prompting for a commit message
        subprocess.run(['git', 'revert', '-n', '-m', '1', commit_hash])

        # Commit the revert and push the changes to the remote repository
        subprocess.run(['git', 'commit', '-m', f"Revert '{commit_hash}'", '--no-edit'])
        subprocess.run(['git', 'push'])

        print(f"Reverted commit {commit_hash}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    revert_last_commit()
