from agency_swarm.agents import Agent
from instructor import llm_validator


class OBDBAccessAgent(Agent):
    def __init__(self):
        super().__init__(
            name="OBDBAccessAgent",
            description="OBDBAccessAgent is an agent with capability to access and search the online Open Brewery "
                        "database.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
            model="gpt-3.5-turbo",
        )

    def response_validator(self, message):
        return message
