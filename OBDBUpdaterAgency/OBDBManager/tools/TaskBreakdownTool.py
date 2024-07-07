from agency_swarm.tools import BaseTool
from pydantic import Field
import re

class TaskBreakdownTool(BaseTool):
    """
    TaskBreakdownTool is designed to break down an overall job description into manageable tasks,
    focusing on one brewery at a time. It takes an overall job description and returns a list of tasks
    specific to each brewery.
    """

    job_description: str = Field(
        ..., description="The overall job description that needs to be broken down into tasks."
    )
    brewery_name: str = Field(
        ..., description="The name of the brewery for which tasks need to be generated."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method breaks down the job description into tasks specific to the given brewery.
        """
        # Extract tasks related to the specified brewery
        tasks = self._extract_tasks_for_brewery(self.job_description, self.brewery_name)
        
        # Return the list of tasks as a string
        return "\n".join(tasks)

    def _extract_tasks_for_brewery(self, job_description, brewery_name):
        """
        Helper method to extract tasks related to the specified brewery from the job description.
        """
        # Split the job description into lines
        lines = job_description.split('\n')
        
        # Initialize a list to hold tasks for the specified brewery
        brewery_tasks = []
        
        # Define a regex pattern to match tasks related to the specified brewery
        pattern = re.compile(rf'\b{re.escape(brewery_name)}\b', re.IGNORECASE)
        
        # Iterate through each line and check if it contains the brewery name
        for line in lines:
            if pattern.search(line):
                brewery_tasks.append(line.strip())
        
        return brewery_tasks