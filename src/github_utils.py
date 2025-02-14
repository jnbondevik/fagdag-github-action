from github import PullRequest, InputGitAuthor, Repository

def get_latest_commit_message(pull_request : PullRequest) -> list[str]:
    return pull_request.get_commits()[-1]

def commit_and_push(repo: Repository, target_branch:str, file_path: str) -> None:
    author = InputGitAuthor(
    "GitHub Action",
    "action@github.com")
    commit_message = "Add haiku art"
    remote_file = repo.get_contents(file_path, ref=target_branch)
    with open(file_path) as f: 
        new_file_content = f.read()
        repo.update_file(
            path=file_path,
            message=commit_message,
            content=new_file_content,
            sha=remote_file.sha,
            branch=target_branch,
            author=author
        )
