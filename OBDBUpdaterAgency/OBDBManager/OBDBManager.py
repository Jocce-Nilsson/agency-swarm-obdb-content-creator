from agency_swarm.agents import Agent


class OBDBManager(Agent):
    def __init__(self):
        super().__init__(
            name="OBDBManager",
            description="Breaks down the job into tasks, one brewery at a time.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
            model="gpt-4o",
        )
        
    def response_validator(self, message):
        return message
