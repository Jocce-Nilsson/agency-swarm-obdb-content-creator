import os
from abc import abstractmethod
from agency_swarm import BaseTool
from github import Github
from github import Auth


class GitHubBaseTool(BaseTool):

    @staticmethod
    def get_github():
        github_access_token: str = os.getenv("GITHUB_ACCESS_TOKEN")
        if not github_access_token:
            raise ValueError("GitHub access token is required for GitHubTool.")
        return Github(auth=Auth.Token(github_access_token))

    @staticmethod
    def get_current_branch(repo):
        branch = repo.git.branch("--show-current")
        if branch.find("csvcreator/") == -1:
            repo.close()
            raise ValueError(f"Branch name must be created first by the tool GitCreateBranchTool.")
        return branch

    @abstractmethod
    def run(self):
        pass


# Example usage
if __name__ == "__main__":
    tool = GitHubBaseTool()
    tool.run()
