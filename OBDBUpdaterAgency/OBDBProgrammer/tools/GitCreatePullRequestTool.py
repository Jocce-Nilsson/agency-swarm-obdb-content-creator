import os
import uuid

from git import Repo, InvalidGitRepositoryError
from pydantic import Field

from OBDBManager.other.BreweryListBaseTool import BreweryListBaseTool
from OBDBProgrammer.other.GitHubBaseTool import GitHubBaseTool


class GitCreatePullRequestTool(GitHubBaseTool):
    """
    GitCreatePullRequestTool is a tool for creating a pull request in a repository.
    - It requires the checkout
    directory where the repository is checked out by the tool GitCheckoutTool.
    - It requires at least one commit made
    by the tool CSVFileProcessorTool.
    - It requires a description between 10 and 30 characters of the changes made in
    the pull request. Example: "Add Blekinge, Sweden".
    The tool will return the URL of the pull request to send to the end user.
    """

    class ToolConfig:
        one_call_at_a_time = True
        strict = True

    checkout_directory: str = Field(
        None, description="The name of the repository checkout directory. Mandatory."
    )
    description: str = Field(
        None, description="The description of the changes made. Mandatory."
    )
    github_repository_name: str = Field(
        "openbrewerydb", description="The name of the target repository. Default is openbrewerydb."
    )
    github_target_repository_owner: str = Field(
        "openbrewerydb", description="The name of the target repository owner. Default is openbrewerydb."
    )
    github_source_repository_owner: str = Field(
        "Jocce-Nilsson", description="The name of the target repository owner. Default is openbrewerydb."
    )

    def run(self):
        if not self.checkout_directory:
            raise ValueError("Field checkout_directory is required for GitCreatePullRequestTool. Run GitCheckoutTool "
                             "first.")
        if not os.path.exists(self.checkout_directory):
            raise ValueError(f"Directory does not exist: {self.checkout_directory}, make sure to run GitCheckoutTool.")
        if not os.path.exists(self.checkout_directory + "/data"):
            raise ValueError(f"Directory does not exist: {self.checkout_directory}/data, make sure to run "
                             "GitCheckoutTool.")
        if not self.description:
            raise ValueError("Field description is required for GitCreatePullRequestTool.")
        if len(self.description) < 10:
            raise ValueError("Field description must be at least 10 characters long.")
        if len(self.description) > 50:
            raise ValueError("Field description must be at most 50 characters long.")
        if not BreweryListBaseTool.is_brewery_list_empty():
            raise ValueError("Brewery list is not empty, please finish processing CSV files first.")
        try:
            repo = Repo(self.checkout_directory)
        except InvalidGitRepositoryError as e:
            raise ValueError(f"{self.checkout_directory} is not a valid git repository. Run GitCheckoutTool first.")
        # validate and get branch name
        current_branch = self.get_current_branch(repo)
        # check for uncommitted changes
        if str(repo.git.status()).find("nothing to commit") == -1:
            repo.close()
            raise ValueError(f"Uncommitted changes in {self.checkout_directory}")
        # compare to master
        if str(repo.git.diff("origin/master", current_branch, "--name-only")).find("data") == -1:
            repo.close()
            raise ValueError(f"No differences to master in branch {current_branch}")
        github = self.get_github()
        print(f"Pushing changes to {current_branch}")
        repo.git.push("origin", current_branch)
        print(f"Creating pull request")
        response = github.get_repo(f"{self.github_source_repository_owner}/{self.github_repository_name}").create_pull(
            title=f"{self.description}", head=f"{current_branch}", draft=True,
            base="master",
            # head_repo=f"{self.github_source_repository_owner}/{self.github_repository_name}",
            body="Automated pull request from Agency Swarm agent OBDBProgrammer.\n"
                 "Containing commits for adding data to the openbrewerydb repository.")
        print(f"Pull request created: {response}")
        repo.close()
        github.close()
        print(response.html_url)
        return response.html_url


# Example usage
if __name__ == "__main__":
    tool = GitCreatePullRequestTool(checkout_directory="/tmp/",
                                    description="Add Skåne, Sweden")
    tool.run()
