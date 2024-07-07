from agency_swarm.tools import BaseTool
from pydantic import Field
from datetime import datetime, timedelta

class TaskMonitoringTool(BaseTool):
    """
    TaskMonitoringTool is designed to ensure that all tasks are completed on time and meet the required standards.
    It monitors the progress of tasks and alerts if any task is behind schedule or does not meet the standards.
    """

    task_deadlines: dict[str, str] = Field(
        ..., description="A dictionary containing tasks and their deadlines. Keys are task descriptions, and values are deadlines in 'YYYY-MM-DD' format."
    )
    task_statuses: dict[str, str] = Field(
        ..., description="A dictionary containing the current status of tasks. Keys are task descriptions, and values are their statuses."
    )
    current_date: str = Field(
        ..., description="The current date in 'YYYY-MM-DD' format for monitoring purposes."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method monitors the progress of tasks and alerts if any task is behind schedule or does not meet the standards.
        """
        # Monitor the tasks and generate alerts
        alerts = self._monitor_tasks(self.task_deadlines, self.task_statuses, self.current_date)
        
        # Return the alerts as a string
        return "\n".join(alerts)

    def _monitor_tasks(self, task_deadlines, task_statuses, current_date):
        """
        Helper method to monitor tasks and generate alerts if any task is behind schedule or does not meet the standards.
        """
        # Convert the current date to a datetime object
        current_date_obj = datetime.strptime(current_date, '%Y-%m-%d')
        
        # Initialize a list to hold alerts
        alerts = []

        # Iterate through each task and its deadline
        for task, deadline in task_deadlines.items():
            # Convert the deadline to a datetime object
            deadline_date_obj = datetime.strptime(deadline, '%Y-%m-%d')
            
            # Check if the task is behind schedule
            if current_date_obj > deadline_date_obj:
                alerts.append(f"Alert: Task '{task}' is behind schedule. Deadline was {deadline}.")
            
            # Check if the task does not meet the required standards
            status = task_statuses.get(task, "Not Started")
            if status not in ["Completed", "In Progress"]:
                alerts.append(f"Alert: Task '{task}' does not meet the required standards. Current status: {status}.")

        return alerts