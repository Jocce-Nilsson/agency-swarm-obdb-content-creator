import os
import uuid
from git import Repo
from pydantic import Field

from OBDBProgrammer.other.GitHubBaseTool import GitHubBaseTool

target_directory: str = ""


class GitCheckoutTool(GitHubBaseTool):
    """
    GitCheckoutTool is a tool for checking out a GitHub repository based on <owner>/<name> defined in field
    github_repository_owner and github_repository_name. Default repository is Jocce-Nilsson/openbrewerydb.
    Mandatory field checkout_directory_parent is the parent directory of the checkout directory structure.
    The function run() will
    - check if the parent directory exists, if not create it
    - create a temporary directory under parent directory, for a unique checkout directory between runs
    - check out the repository under the temporary directory and return the name of the checkout directory
    """

    class ToolConfig:
        one_call_at_a_time = True
        strict = True

    checkout_directory_parent: str = Field(
        "/tmp", description="The parent directory of the checkout directory structure where the "
                            "repository is checked out. Default is /tmp. Do not change this unless specified."
    )
    github_repository_name: str = Field(
        "openbrewerydb", description="The name of the repository to check out. Default is openbrewerydb."
    )
    github_repository_owner: str = Field(
        "Jocce-Nilsson", description="The name of the repository to check out. Default is Jocce-Nilsson."
    )

    def run(self):
        global target_directory
        if target_directory:
            print(f"Already checked out repository {self.github_repository_owner}/{self.github_repository_name} into "
                  f"directory: {target_directory}")
            return target_directory
        if not self.checkout_directory_parent:
            raise ValueError("Field checkout_directory_parent is required for GitCheckoutTool.")
        if not os.path.exists(self.checkout_directory_parent):
            print(f"Creating directory: {self.checkout_directory_parent}")
            os.makedirs(self.checkout_directory_parent)
        random_dir_name = f"{self.checkout_directory_parent}/{uuid.uuid4()}/"
        os.makedirs(random_dir_name)
        print(f"Created directory: {random_dir_name}")
        repo_name = f"{self.github_repository_owner}/{self.github_repository_name}"
        print(f"Checking out repository: {repo_name}")
        print(f"    Desc: {self.get_github().get_repo(repo_name).description}")
        target_directory = os.path.join(random_dir_name, self.github_repository_name)
        print(f"    Into: {target_directory}")
        repo = Repo.clone_from(f"https://github.com/{self.github_repository_owner}/{self.github_repository_name}",
                               target_directory)
        print(f"    Done")
        print(f"    HEAD: {repo.head.commit.hexsha}")
        repo.close()
        print(f"Checked out repository {repo_name} into directory: {target_directory}")
        return target_directory


# Example usage
if __name__ == "__main__":
    if os.path.exists("./tmp/"):
        import shutil
        shutil.rmtree("./tmp/")
    tool = GitCheckoutTool(checkout_directory_parent="./tmp")
    tool.run()
