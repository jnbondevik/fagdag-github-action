import os
from github import Github, Auth
import pyfiglet 
from haiku_checker import is_haiku
from github_utils import commit_and_push, get_latest_commit_message

if __name__ == '__main__':

    acces_token = os.environ.get('GITHUB_TOKEN')
    repo_uri = os.environ.get('GITHUB_REPOSITORY')
    pr_number = int(os.environ.get('PR_NUMBER'))

    if(repo_uri is None or acces_token is None):
        raise Exception('Could not find repository')
    
    token = Auth.Token(acces_token)
    github = Github(auth=token)
    
    repo = github.get_repo(repo_uri)
    pull_request = repo.get_pull(pr_number)
    branch = pull_request.head.ref 
    
    file_path = "poetry.md".replace("/github/workspace/", "")
    
    #TODO 
    # 1) Get the latest commit message
    last_commit = get_latest_commit_message(pull_request)
    # 2) Check if the commit message follows the haiku format
    commit_is_haiku = is_haiku(last_commit)
    # 3) If this is the case:
    #      - Generate ascii art from the commit message using pyfiglet 
    #      - Write the ascii art to haiku.md
    #      - Commit and push the results!      
    if commit_is_haiku:
        ascii_message = pyfiglet.Figlet.renderText(last_commit)
        with open(file_path, 'w') as outfile:
            outfile.write(ascii_message)
        commit_and_push(repo, branch, file_path)
