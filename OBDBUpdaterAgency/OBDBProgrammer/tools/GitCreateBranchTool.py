import os

from agency_swarm import BaseTool
from git import Repo
from pydantic import Field
from unidecode import unidecode

branch_name = ""


class GitCreateBranchTool(BaseTool):
    """
    GitCreateBranchTool is a tool for creating a branch in a repository.
    - It requires the parent directory of the checkout directory where the repository is checked out.
    - It requires a description between 10 and 30 characters of the changes to be made in the branch
      as a base for the branch name. Example: "Add Blekinge, Sweden".
    Non unicode characters are converted to unicode in the description, then converted to lowercase,
    finally spaces are replaced with underscores to form last part of the branch name.
    - The tool returns the name of the branch created.
    """

    class ToolConfig:
        one_call_at_a_time = True
        strict = True

    checkout_directory: str = Field(
        None, description="The name of the repository checkout directory. Mandatory."
    )
    description: str = Field(
        None, description="The description of the changes to be made in the branch. Mandatory."
    )

    def branch_name(self):
        # Convert to unicode and lowercase; Ceñía -> cenia
        desc = unidecode(self.description)
        # Replace spaces with underscores
        desc = desc.replace(' ', '_').lower()
        # Remove all rest but underscore (95) and a-z (97-122)
        desc = ''.join([i if 94 < ord(i) < 123 else '' for i in desc])
        desc = desc.replace('`', '').lower()  # Remove backticks (96)
        if len(desc) < 5:
            raise ValueError("Remaining branch name after simplification is too short. Please provide a longer "
                             "description.")
        return f"csvcreator/{desc}"

    def run(self):
        global branch_name
        if branch_name:
            print(f"Branch already exists: {branch_name}")
            return branch_name
        if not self.checkout_directory:
            raise ValueError("Field checkout_directory is required for GitCreateBranchTool.")
        if not os.path.exists(self.checkout_directory):
            raise ValueError(f"Directory does not exist: {self.checkout_directory}, make sure to run GitCheckoutTool.")
        if not self.description:
            raise ValueError("Field description is required for GitCreateBranchTool.")
        if len(self.description) < 10:
            raise ValueError("Field description must be at least 10 characters long.")
        if len(self.description) > 30:
            raise ValueError("Field description must be at most 30 characters long.")
        repo = Repo(self.checkout_directory)
        branch_name = self.branch_name()
        for name in repo.branches:
            if branch_name.find(str(name)) != -1:
                print(f"Branch already exists: {branch_name}")
                repo.close()
                return branch_name
        print(f"Creating branch: {branch_name}")
        repo.git.checkout("HEAD", b=branch_name)
        repo.close()
        return branch_name


# Example usage
if __name__ == "__main__":
    tool = GitCreateBranchTool(checkout_directory="./tmp/dcd75a42-513a-4fcd-b615-0fccfd9d2faa/openbrewerydb",
                               description="Add Skåne, Sweden")
    tool.run()
