from agency_swarm.tools import BaseTool
from pydantic import Field

class TaskAssignmentTool(BaseTool):
    """
    TaskAssignmentTool is designed to assign tasks to the OBDBProgrammer and OBDBController.
    It takes a list of tasks and assigns them to the appropriate agent based on predefined criteria.
    """

    tasks: list[str] = Field(
        ..., description="A list of tasks that need to be assigned to agents."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method assigns tasks to the OBDBProgrammer and OBDBController based on predefined criteria.
        """
        # Assign tasks to the appropriate agents
        assignments = self._assign_tasks(self.tasks)
        
        # Return the assignments as a string
        return "\n".join(assignments)

    def _assign_tasks(self, tasks):
        """
        Helper method to assign tasks to the OBDBProgrammer and OBDBController based on predefined criteria.
        """
        # Initialize lists to hold tasks for each agent
        programmer_tasks = []
        controller_tasks = []

        # Define criteria for task assignment
        programmer_keywords = ['develop', 'code', 'program', 'implement']
        controller_keywords = ['manage', 'control', 'oversee', 'monitor']

        # Iterate through each task and assign it to the appropriate agent
        for task in tasks:
            if any(keyword in task.lower() for keyword in programmer_keywords):
                programmer_tasks.append(f"OBDBProgrammer: {task}")
            elif any(keyword in task.lower() for keyword in controller_keywords):
                controller_tasks.append(f"OBDBController: {task}")
            else:
                # If no specific keywords are found, assign to a default agent (e.g., OBDBController)
                controller_tasks.append(f"OBDBController: {task}")

        # Combine the assignments into a single list
        assignments = programmer_tasks + controller_tasks
        
        return assignments