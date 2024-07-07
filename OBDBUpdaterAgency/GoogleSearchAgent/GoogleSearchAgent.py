from agency_swarm.agents import Agent


class GoogleSearchAgent(Agent):
    def __init__(self):
        super().__init__(
            name="GoogleSearchAgent",
            description="Agent for searching the web",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )
        from OBDBUpdaterAgency.GoogleSearchAgent.tools.GoogleSearchTool import GoogleSearchTool
        GoogleSearchTool().validate_required_environment_variables()
        
    def response_validator(self, message):
        return message
