from agency_swarm.tools import BaseTool
from pydantic import Field

class ProgressReportingTool(BaseTool):
    """
    ProgressReportingTool is designed to coordinate with OBDBCEO to report progress and any issues.
    It takes the current status of tasks and generates a report to be sent to the OBDBCEO.
    """

    task_statuses: dict[str, str] = Field(
        ..., description="A dictionary containing the current status of tasks. Keys are task descriptions, and values are their statuses."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method generates a progress report based on the current status of tasks.
        """
        # Generate the progress report
        report = self._generate_report(self.task_statuses)
        
        # Return the report as a string
        return report

    def _generate_report(self, task_statuses):
        """
        Helper method to generate a progress report based on the current status of tasks.
        """
        # Initialize the report with a header
        report_lines = ["Progress Report for OBDBCEO", "===========================", ""]

        # Iterate through each task and its status
        for task, status in task_statuses.items():
            report_lines.append(f"Task: {task}")
            report_lines.append(f"Status: {status}")
            report_lines.append("")

        # Combine the report lines into a single string
        report = "\n".join(report_lines)
        
        return report